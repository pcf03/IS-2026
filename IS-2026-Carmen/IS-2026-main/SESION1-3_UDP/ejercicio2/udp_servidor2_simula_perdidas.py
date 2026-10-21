import socket
import sys
import random

if len(sys.argv) > 1:
    puerto = int(sys.argv[1])

else: 
    puerto = 9999


servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
servidor.bind(("", puerto))

print("Servidor UDP esperando mensajes...")

while True:
    datagrama, direccion = servidor.recvfrom(1024)
    mensaje = datagrama.dercode("utf-8")

    # para simular la perdida...
    # elegimos aleatorio entre 0 y 1
    # si sale 0, el paquete se pierde
    if random.randint(0, 1) == 0:
        print("Simulando paquete perdido")
    
    # si sale 1, mensaje normal
    else:
        print("Recibido desde: ", origen)
        print(mensaje)
