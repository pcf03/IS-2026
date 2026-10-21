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
    datos, direccion = servidor.recvfrom(1024)

    if random.randint(0, 1) == 0:
        print("Simulando paquete perdido")
    else:
        print(datos.decode())
        servidor.sendto("OK".encode("utf-8"), direccion)
        
