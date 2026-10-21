import socket
import sys

# elegimos IP del servidor
if len(sys.argv) > 1:
    ip = sys.argv[1]

else: # si no pasamos ninguna como parametro...
    ip = "localhost"

# elegimos puerto
if len(sys.argv) > 2:
    puerto = int(sys.argv[2]) # hay que pasarlo a entero

else:
    puerto = 9999

# CREAMOS SOCKET UDP (usando IPv4)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# socket.AF_INET -> indica que usamos IPv4
# socket.SOCK_DGRAM -> indica que queremos un socket de datagramas -> UDP

while True:

    # Pedimos el mensaje a enviar
    mensaje = input("Escribe un mensaje: ")

    # Si es FIN, terminamos
    if mensaje == "FIN":
        break

    # Convertimos el mensaje a bytes y lo enviamos al servidor
    s.sendto(mensaje.encode("utf-8"), (ip, puerto))

s.close()