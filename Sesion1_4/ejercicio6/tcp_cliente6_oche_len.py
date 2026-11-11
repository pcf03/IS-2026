import socket
import sys

ip = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
puerto = int(sys.argv[2]) if len(sys.argv) > 2 else 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, puerto))

# Convertimos a fichero para leer las respuestas fácilmente
f = s.makefile(encoding="utf8", newline="\n")

mensajes = ["HOLA", "ESTO", "ES", "SEGURO"]

for palabra in mensajes:
    palabra_bytes = palabra.encode("utf8")
    # 1. Calculamos la longitud en bytes y creamos la cabecera ASCII con \n
    longitud_str = f"{len(palabra_bytes)}\n"
    
    # 2. Enviamos todo junto (longitud ASCII + mensaje)
    s.sendall(longitud_str.encode("utf8") + palabra_bytes)

# Recibimos las respuestas
for _ in mensajes:
    # Leemos la longitud hasta el \n
    linea_longitud = f.readline()
    if not linea_longitud:
        break
        
    longitud = int(linea_longitud)
    # Leemos exactamente los caracteres de la respuesta
    respuesta = f.read(longitud)
    print(f"Recibido: {respuesta}")

f.close()
s.close()