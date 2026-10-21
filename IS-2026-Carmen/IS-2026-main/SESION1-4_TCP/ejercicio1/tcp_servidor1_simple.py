import socket
import sys

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
        datos = sd.recv(5)  # Observar que se lee del socket sd, no de s
        mensaje = datos.decode("ascii") # Pasar los bytes a caracteres
                # En este ejemplo se asume que el texto recibido es ascii puro

        # si recibimos cadena vacía = conexion cerrada
        if mensaje == "":
            print("Conexion cerrada de forma inesperada por el cliente")
            sd.close()
            continuar = False

        # si recibimos FIN, terminamos conexion
        elif mensaje == "FINAL":
            print("Recibido mensaje de finalización")
            sd.close()
            continuar = False

        # si es un mensaje normal, print
        else:
            print("Recibido mensaje:", mensaje)