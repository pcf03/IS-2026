import socket
import sys

def recibe_mensaje(sock):
    buffer = []
    while True:
        byte = sock.recv(1)
        if not byte:
            return b""
        buffer.append(byte)
        if byte == b"\n":
            break
    return b"".join(buffer)

ip = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
puerto = int(sys.argv[2]) if len(sys.argv) > 2 else 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, puerto))

mensajes = ["UNO", "DOS", "TRES"]

# 1. Enviamos los tres mensajes seguidos, ametrallando al servidor[cite: 9]
for palabra in mensajes:
    s.sendall((palabra + "\r\n").encode("utf8"))

# 2. Leemos las respuestas usando la función robusta
for _ in range(3):
    respuesta_bytes = recibe_mensaje(s)
    if not respuesta_bytes:
        break
    respuesta = respuesta_bytes.decode("utf8")
    print(f"Recibido: {repr(respuesta)}")

s.close()