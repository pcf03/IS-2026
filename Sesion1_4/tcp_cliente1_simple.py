import socket
import sys

ip = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
puerto = int(sys.argv[2]) if len(sys.argv) > 2 else 9999

# Crear socket TCP y conectar al servidor[cite: 4]
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, puerto))

# Enviar 5 mensajes de 5 bytes[cite: 4]
for _ in range(5):
    s.send(b"ABCDE")

# Enviar marca de fin y cerrar[cite: 4]
s.send(b"FINAL")
s.close()