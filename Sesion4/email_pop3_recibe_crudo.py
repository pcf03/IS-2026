import socket
import ssl
import sys
import os

def RecvReply(sock):
    respuesta = sock.recv(4096)
    print("Recibido:", respuesta.decode("utf-8", errors="ignore"))
    if not respuesta.startswith(b"+OK"):
        print("Error: El servidor devolvió una respuesta negativa.")
        sys.exit(1)
    return respuesta

# Leer credenciales de las variables de entorno
username = os.environ.get("GMAIL_USER")
password = os.environ.get("GMAIL_APP_PASSWORD")

if not username or not password:
    print("ERROR: Faltan las variables de entorno GMAIL_USER o GMAIL_APP_PASSWORD.")
    sys.exit(1)

server = "pop.gmail.com"
port = 995

# 1. Crear conexión TCP y envolverla con SSL
print(f"Conectando a {server}:{port} de forma segura...")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((server, port))

context = ssl.create_default_context()
sc = context.wrap_socket(s, server_hostname=server)

# Leer mensaje de bienvenida del servidor POP3 (+OK)
RecvReply(sc)

# 2. Enviar comando USER
print("Enviando USER...")
sc.sendall(f"USER {username}\r\n".encode("ascii"))
RecvReply(sc)

# 3. Enviar comando PASS
print("Enviando PASS...")
sc.sendall(f"PASS {password}\r\n".encode("ascii"))
RecvReply(sc)

# 4. Enviar comando STAT para ver cuántos mensajes hay
print("Enviando STAT...")
sc.sendall(b"STAT\r\n")
respuesta_stat = RecvReply(sc)

# 5. Obtener el primer mensaje con RETR 1
print("Solicitando el primer mensaje (RETR 1)...")
sc.sendall(b"RETR 1\r\n")
# Recibimos hasta que termine con \r\n.\r\n
mensaje_bytes = b""
while not mensaje_bytes.endswith(b"\r\n.\r\n"):
    chunk = sc.recv(4096)
    if not chunk:
        break
    mensaje_bytes += chunk

print("\n--- CONTENIDO DEL PRIMER MENSAJE RECIBIDO ---")
print(mensaje_bytes.decode("utf-8", errors="ignore")[:500]) # Mostramos los primeros 500 caracteres

# 6. Terminar la sesión con QUIT
print("\nEnviando QUIT...")
sc.sendall(b"QUIT\r\n")
RecvReply(sc)

sc.close()
print("¡Sesión POP3 cerrada con éxito!")