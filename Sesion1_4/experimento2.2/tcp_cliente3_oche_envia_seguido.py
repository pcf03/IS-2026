import socket
import sys

ip = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
puerto = int(sys.argv[2]) if len(sys.argv) > 2 else 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, puerto))

mensajes = ["UNO", "DOS", "TRES"]

# 1. Enviar los tres mensajes en rápida sucesión[cite: 9]
for palabra in mensajes:
    s.sendall((palabra + "\r\n").encode("utf8"))

# 2. Intentar leer las respuestas
for _ in range(3):
    respuesta_bytes = s.recv(80)
    if not respuesta_bytes:
        break
    respuesta = respuesta_bytes.decode("utf8")
    # Usamos repr() para ver exactamente qué nos ha llegado, incluyendo los \r\n ocultos[cite: 9]
    print(f"Recibido: {repr(respuesta)}")

s.close()