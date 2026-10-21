import socket
import random
import sys

if len(sys.argv) > 1:
    puerto = int(sys.argv[1])

else: 
    puerto = 9999

servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
servidor.bind(("", puerto))

print("Servidor UDP esperando mensajes...")

while True:
    datagrama, origen = servidor.recvfrom(1024)

    mensaje = datagrama.decode("utf-8")

    if random.randint(0, 1) == 0:
        print("Simulando paquete perdido")

    else:
        print("Recibido desde: ", origen)
        print(mensaje)

        # sacamos el id que aparece
        identificador = mensaje.split(":")[0]

        # confirmacion que contiene ese id
        confirmacion = "OK" + identificador

        # enviamos confirmacion al cliente
        servidor.sendto(confirmacion.encode("utf-8"), direccion)
        
