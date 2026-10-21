import socket
import sys

# el cliente recibe la direccion broadcast
if len(sys.argv) > 1:
    ip = sys.argv[1]
else:
    print("Debes indicar la dirección de broadcast")
    sys.exit()

puerto = 12345 #porque siempre es este

cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# activamos broadcast
cliente.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

# enviamos BUSCANDO HOLA a todos los equipos de la red
mensaje = "BUSCANDO HOLA"

cliente.sendto(mensaje.encode("utf-8"),(ip, puerto))

# aqui guardamos la IP del primer servidor que responda
primer_servidor = None

# ponemos el timeout
cliente.settimeout(1)

# recibimos respuestas de los servidores
while True:

    try:
        datagrama, origen = cliente.recvfrom(1024)
        mensaje = datagrama.decode("utf-8")


        if mensaje == "IMPLEMENTO HOLA":
            print("Servidor encontrado: ", origen[0])

            if primer_servidor is None:
                primer_servidor = origen[0]


    except socket.timeout:
        break

# si al menos uno responde, usamos el primero
if primer_servidor is not None:
    mensaje = "HOLA"

    cliente.sendto(mensaje.encode("utf-8"), (primer_servidor, puerto))

    # ya no necesitamos el timeout para esta parte
    cliente.settimeout(None)

    # esperamos la respuesta del servidor elegido
    datagrama, origen = cliente.recvfrom(1024)

    mensaje = datagrama.decode("utf-8")

    print("Respuesta del servidor: ", mensaje)

else:
    print("No se ha encontrado ningún servidor HOLA")

cliente.close()