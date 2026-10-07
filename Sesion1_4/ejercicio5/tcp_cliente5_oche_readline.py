import socket
import sys

ip = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
puerto = int(sys.argv[2]) if len(sys.argv) > 2 else 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, puerto))

# Convertimos nuestro extremo del socket a fichero para leer fácilmente las respuestas[cite: 11]
f = s.makefile(encoding="utf8", newline="\r\n")

mensajes = ["UNO", "DOS", "TRES"]

for palabra in mensajes:
    s.sendall((palabra + "\r\n").encode("utf8"))

for _ in range(3):
    # readline() ya nos devuelve un string (str), nos ahorramos el decode[cite: 11, 12]
    respuesta = f.readline()
    if not respuesta:
        break
    print(f"Recibido: {repr(respuesta)}")

f.close()
s.close()