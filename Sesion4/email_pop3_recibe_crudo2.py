import socket
import ssl
import sys
import os

def RecvReply(sock):
    respuesta = sock.recv(4096)
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

print(f"Conectando a {server}:{port} de forma segura...")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((server, port))

context = ssl.create_default_context()
sc = context.wrap_socket(s, server_hostname=server)

RecvReply(sc)

# Autenticación
sc.sendall(f"USER {username}\r\n".encode("ascii"))
RecvReply(sc)

sc.sendall(f"PASS {password}\r\n".encode("ascii"))
RecvReply(sc)

# Obtener número total de mensajes con STAT
sc.sendall(b"STAT\r\n")
resp_stat = RecvReply(sc).decode("utf-8")
# La respuesta típica es "+OK num_mensajes num_bytes"
partes = resp_stat.split()
num_mensajes = int(partes[1])

print(f"\n--- Total de mensajes en el buzón: {num_mensajes} ---")
print("Buscando Asunto y Remitente de cada mensaje...\n")

# Bucle para recorrer los mensajes (por seguridad con tantos mensajes, limitamos a los 10 primeros si son muchos, o los recorremos todos)
limite = min(num_mensajes, 10) # Mostramos los 10 primeros para no saturar la pantalla

for i in range(1, limite + 1):
    # Usamos TOP para traernos solo las cabeceras y las primeras líneas (ahorra ancho de banda)
    sc.sendall(f"TOP {i} 0\r\n".encode("ascii"))
    
    cabeceras_bytes = b""
    while not cabeceras_bytes.endswith(b"\r\n.\r\n"):
        chunk = sc.recv(4096)
        if not chunk:
            break
        cabeceras_bytes += chunk
        
    # Extraer Subject y From buscando línea a línea
    lineas = cabeceras_bytes.decode("utf-8", errors="ignore").split("\r\n")
    asunto = "<Sin asunto>"
    remitente = "<Desconocido>"
    
    for linea in lineas:
        if linea.lower().startswith("subject:"):
            asunto = linea[8:].strip()
        elif linea.lower().startswith("from:"):
            remitente = linea[5:].strip()
            
    print(f"[{i}] From: {remitente}")
    print(f"    Subject: {asunto}")
    print("-" * 40)

# Cerrar sesión
sc.sendall(b"QUIT\r\n")
RecvReply(sc)
sc.close()
print("\n¡Lectura masiva de cabeceras finalizada!")