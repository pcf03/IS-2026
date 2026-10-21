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

cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

contador = 1

while True:
    mensaje = input("Escribe un mensaje: ")

    if mensaje == "FIN":
        break

    datagrama = str(contador) + ": " + mensaje

    cliente.sendto(datagrama.encode(), (host, puerto))

    cliente.settimeout(0.1) # espero por el OK

    try:
        # esperamos respuesta del servidor
        respuesta, origen = cliente.recvfrom(1024)

        # convertimos bytes recibidos a texto
        respuesta = respuesta.decode("utf-8")

        if respuesta == "OK": # Si llega el OK, confirmo
            print("Recibida confirmación")

    except socket.timeout: # Si no llega nada y se agota el tiempo
        # generamos excepcion socket.timeout
        print("ERROR. El datagrama de confirmación no llega")

    contador += 1

cliente.close()