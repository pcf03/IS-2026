import socket
import sys

ip = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
puerto = int(sys.argv[2]) if len(sys.argv) > 2 else 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, puerto))
f = s.makefile(encoding="utf8")

mensajes = ["HOLA", "ESTO", "ES", "SEGURO"]

for palabra in mensajes:
    # 1. Calculamos la longitud en bytes del mensaje y le añadimos el \n[cite: 13]
    longitud_str = f"{len(palabra.encode('utf8'))}\n"
    
    # 2. Enviamos la concatenación de la longitud y el mensaje[cite: 13]
    s.sendall((longitud_str + palabra).encode("utf8"))

# Recibimos las respuestas con la misma lógica
for _ in mensajes:
    linea_longitud = f.readline()
    if not linea_longitud:
        break
        
    longitud = int(linea_longitud)
    respuesta = f.read(longitud)
    print(f"Recibido: {respuesta}")

f.close()
s.close()