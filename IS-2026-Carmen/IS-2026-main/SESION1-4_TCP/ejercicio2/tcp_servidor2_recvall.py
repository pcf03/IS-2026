import socket
import sys

# funcion recvall()
def recvall(socket_cliente, cantidad):
    datos = b""

    # seguimos recibiendo hasta llegar a todos los bytes
    while len(datos) < cantidad:

        # intentamos recibir solamente los bytes que nos faltan
        bloque = socket_cliente.recv(cantidad-len(datos))

        # si recv devuelve vacío, el cliente ha cerrado la conexión
        if bloque == b"":
            return b""

        # añadimos los nuevos bytes a los que ya teníamos
        datos = datos + bloque

    return datos


if len(sys.argv) > 1:
    puerto = int(sys.argv[1])
else:
    puerto = 9999

# creamos socket TCP utilizando IPv4
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(("", puerto))

# el socket escucha en modo pasivo
s.listen(5) # max 5 clientes pendientes en cola

print("Servidor TCP esperando clientes...")

while True:
    print("Esperando cliente...")

    # esperamos a que se conecte alguien
    # sd será el socket utilizado para comunicarnos con él
    sd, origen = s.accept()

    print("Nuevo cliente conectado desde: ", origen)

    # controlamos si seguimos con ese cliente
    continuar = True

    # recibimos mensajes del cliente conectado
    while continuar:

        # recibimos exactamente 5 bytes usando revall()
        datos = recvall(sd, 5) 
       
        # si recibimos cadena vacía = conexion cerrada
        if datos == b"":
            print("Conexion cerrada de forma inesperada por el cliente")
            sd.close()
            continuar = False

        # si recibimos FIN, terminamos conexion
        else:
            mensaje = datos.decode("ascii")   

            if mensaje == "FINAL":
                print("Recibido mensaje de finalización")
                sd.close()
                continuar = False

        # si es un mensaje normal, print
            else:
                print("Recibido mensaje:", mensaje)