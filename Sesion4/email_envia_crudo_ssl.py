import socket
import sys
import ssl
import base64
import os

def RecvReply(sock, code):
    respuesta = sock.recv(1024)
    print("Recibido:", respuesta.decode("utf-8", errors="ignore"))
    three_bytes = respuesta[:3]
    if three_bytes != code:
        print(f"Error: Se esperaba el código {code.decode()}, pero se recibió {three_bytes.decode()}")
        sys.exit(1)

# Leer credenciales desde las variables de entorno
username = os.environ.get("GMAIL_USER")
password = os.environ.get("GMAIL_APP_PASSWORD")

if not username or not password:
    print("ERROR: Faltan las variables de entorno GMAIL_USER o GMAIL_APP_PASSWORD.")
    sys.exit(1)

server = "smtp.gmail.com"
port = 587

fromaddr = username
toaddr = input("Introduce el correo de destino: ")
subject = "Prueba SMTP seguro con Gmail y sockets - IS"
data = "Hola, este es un correo de prueba enviado mediante sockets seguros con STARTTLS y Gmail usando variables de entorno."

# 1. Conexión TCP normal al puerto 587
print(f"Conectando a {server}:{port}...")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((server, port))
RecvReply(s, b"220")

# 2. Iniciar conversación con EHLO y solicitar STARTTLS
print("Enviando EHLO...")
s.sendall(b"EHLO localhost\r\n")
RecvReply(s, b"250")

print("Enviando STARTTLS...")
s.sendall(b"STARTTLS\r\n")
RecvReply(s, b"220")

# 3. Envolver el socket con SSL para crear el canal seguro
print("Negociando canal seguro SSL...")
context = ssl.create_default_context()
sc = context.wrap_socket(s, server_hostname=server)

# 4. Volver a enviar EHLO a través del canal seguro cifrado
print("Enviando EHLO cifrado...")
sc.sendall(b"EHLO localhost\r\n")
RecvReply(sc, b"250")

# 5. Autenticación AUTH LOGIN
print("Enviando AUTH LOGIN...")
sc.sendall(b"AUTH LOGIN\r\n")
RecvReply(sc, b"334")

print("Enviando usuario en base64...")
sc.sendall(base64.b64encode(username.encode("ascii")) + b"\r\n")
RecvReply(sc, b"334")

print("Enviando contraseña en base64...")
sc.sendall(base64.b64encode(password.encode("ascii")) + b"\r\n")
RecvReply(sc, b"235")

# 6. Comandos estándar de envío de correo
print("Enviando MAIL FROM...")
sc.sendall(f"MAIL FROM: <{fromaddr}>\r\n".encode("utf-8"))
RecvReply(sc, b"250")

print("Enviando RCPT TO...")
sc.sendall(f"RCPT TO: <{toaddr}>\r\n".encode("utf-8"))
RecvReply(sc, b"250")

print("Enviando DATA...")
sc.sendall(b"DATA\r\n")
RecvReply(sc, b"354")

# Construir el mensaje cumpliendo el formato
message = f"To: {toaddr}\r\nFrom: {fromaddr}\r\nSubject: {subject}\r\n\r\n{data}\r\n.\r\n"
sc.sendall(message.encode("utf-8"))
RecvReply(sc, b"250")

print("Enviando QUIT...")
sc.sendall(b"QUIT\r\n")
RecvReply(sc, b"221")

sc.close()
print("¡Correo enviado con éxito a través de Gmail utilizando sockets seguros!")