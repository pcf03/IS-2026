import socket
import sys

if len(sys.argv) > 1:
    ip = sys.argv[1]
else:
    ip = "localhost"

if len(sys.argv) > 2:
    puerto = int(sys.argv[2])
else:
    puerto = 9999

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# establecemos conexion con el servidor
cliente.connect((ip, puerto))

# enviamos los 5 ABCDE
for i in range (5):
    mensaje = "ABCDE"

    # sendall garantiza que se envían todos los bytes
    cliente.sendall(mensaje.encode("ascii"))

mensaje = "FINAL"
cliente.send(mensaje.encode("ascii"))

cliente.close()