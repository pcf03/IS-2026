import socket
import random
import sys

puerto = 12345 #puerto fijo 


servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# ahora activamos broadcast
servidor.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
servidor.bind(("", puerto))

print("Servidor HOLA esperando mensajes...")

while True:
    datagrama, origen = servidor.recvfrom(1024)

    mensaje = datagrama.decode("utf-8")

    print("Recibido desde: ", origen)
    print("Mensaje: ", mensaje)
    
    # si un cliente busca el servidor, le decimos que es este
    if mensaje == "BUSCANDO HOLA":
        respuesta = "IMPLEMENTO HOLA"
        servidor.sendto(respuesta.encode("utf-8"), origen)

    # si el cliente nos elije y solicita HOLA
    elif mensaje == "HOLA":
        # le contestamos con su IP
        respuesta  = "HOLA: " + origen[0]
        servidor.sendto(respuesta.encode("utf-8"), origen)
