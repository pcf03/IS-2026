import socket
import sys
import struct

def recvall(sock, count):
    buf = b''
    while len(buf) < count:
        newbuf = sock.recv(count - len(buf))
        if not newbuf: 
            return b''
        buf += newbuf
    return buf

ip = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
puerto = int(sys.argv[2]) if len(sys.argv) > 2 else 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, puerto))

mensajes = ["HOLA", "ESTO", "ES", "BINARIO"]

# Enviar los mensajes
for palabra in mensajes:
    palabra_bytes = palabra.encode("utf8")
    
    # Empaquetamos la longitud en 2 bytes binarios[cite: 14]
    longitud_bytes = struct.pack(">H", len(palabra_bytes))
    
    # Enviamos la cabecera binaria seguida del texto[cite: 14]
    s.sendall(longitud_bytes + palabra_bytes)

# Recibir las respuestas
for _ in mensajes:
    len_bytes = recvall(s, 2)
    if not len_bytes:
        break
        
    longitud = struct.unpack(">H", len_bytes)[0]
    respuesta = recvall(s, longitud).decode("utf8")
    print(f"Recibido: {respuesta}")

s.close()