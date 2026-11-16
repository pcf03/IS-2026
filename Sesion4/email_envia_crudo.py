import socket
import sys

def RecvReply(s, code):
    # Recibe hasta 1024 bytes del socket
    respuesta = s.recv(1024)
    print("Recibido:", respuesta.decode("utf-8", errors="ignore"))
    
    # Extrae los tres primeros bytes para verificar el código de respuesta esperado
    three_bytes = respuesta[:3]
    if three_bytes != code:
        print(f"Error: Se esperaba el código {code.decode()}, pero se recibió {three_bytes.decode()}")
        sys.exit(1)

# 2. Definición de variables de configuración
server = "relay.uniovi.es"
port = 25
fromaddr = "uo287992@uniovi.es"   # Pon aquí tu correo de Uniovi
toaddr = "uo287992@uniovi.es"     # Pon aquí tu correo de destino en Uniovi
subject = "Prueba de correo SMTP en crudo - IS"
data = "Hola, este es un mensaje de prueba enviado mediante un socket TCP crudo en la Sesión 4."

# 3. Crear conexión TCP al servidor SMTP
print(f"Conectando a {server}:{port}...")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((server, port))

# Leer el mensaje de bienvenida del servidor (código 220)
RecvReply(s, b"220")

# 4. Enviar comandos SMTP secuencialmente
print("Enviando HELO...")
s.sendall(b"HELO localhost\r\n")
RecvReply(s, b"250")

print("Enviando MAIL FROM...")
s.sendall(f"MAIL FROM: <{fromaddr}>\r\n".encode("utf-8"))
RecvReply(s, b"250")

print("Enviando RCPT TO...")
s.sendall(f"RCPT TO: <{toaddr}>\r\n".encode("utf-8"))
RecvReply(s, b"250")

print("Enviando DATA...")
s.sendall(b"DATA\r\n")
RecvReply(s, b"354")

# Construir el mensaje cumpliendo el formato con cabeceras, \r\n\r\n y \r\n.\r\n al final
message = f"To: {toaddr}\r\nFrom: {fromaddr}\r\nSubject: {subject}\r\n\r\n{data}\r\n.\r\n"
s.sendall(message.encode("utf-8"))
RecvReply(s, b"250")

print("Enviando QUIT...")
s.sendall(b"QUIT\r\n")
RecvReply(s, b"221")

s.close()
print("¡Correo enviado con éxito a través de sockets en crudo!")