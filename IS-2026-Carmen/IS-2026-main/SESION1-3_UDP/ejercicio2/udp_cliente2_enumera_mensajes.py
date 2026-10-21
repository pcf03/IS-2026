import socket
import sys

if len(sys.argv) > 1:
    ip = sys.argv[1]

else: 
    ip = "localhost"

cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# este será el numero que identifique cada mensaje
contador = 1

while True:
    mensaje = input("Escribe un mensaje: ")

    if mensaje == "FIN":
        break

    # ahora añadimos el numero delante del mensaje
    datagrama = str(contador) + ": " + mensaje

    cliente.sendto(datagrama.encode(), (host, puerto))

    # incrementamos el contador a 1
    contador += 1

cliente.close()