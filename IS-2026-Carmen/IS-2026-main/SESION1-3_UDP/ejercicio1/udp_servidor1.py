import socket
import sys

if len(sys.argv) > 1:
    puerto = int(sys.argv[1])

else: 
    puerto = 9999

# Creamos socket UDP con IPv4
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# asociamos el socket al puerto indicado
# "" significa escuchar en todas las inetrfaces de red de la máquina
s.bind(("", puerto))

print(f"Servidor UDP escuchando en el puerto", puerto)

while True:
    # esperamos un datagrama de 1024 bytes
    # y obtenemos la IP y puerto desde donde se envió
    datagrama, origen = s.recvfrom(1024)

    # convertimos bytes a str
    mensaje = datagrama.decode("utf-8")

    print ("Recibido desde: ", origen)
    print(mensaje);
