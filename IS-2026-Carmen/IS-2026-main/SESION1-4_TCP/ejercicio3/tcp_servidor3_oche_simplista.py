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

print("Servidor OCHE esperando clientes...")

while True:
    print("Esperando cliente...")

    # esperamos a que se conecte alguien
    # sd será el socket utilizado para comunicarnos con él
    sd, origen = s.accept()

    print("Nuevo cliente conectado desde: ", origen)

    # recibimos mensajes del cliente hasta que cierre conexion
    while True:

        # recibimos exactamente 5 bytes usando revall()
        mensaje = sd.recv(80) 
       
        # si recibimos cadena vacía = conexion cerrada
        if mensaje == b"":
            print("Conexion cerrada de forma inesperada por el cliente")
            break


        mensaje = mensaje.decode("utf-8")   

        # quitamos los 2 ultimos caracteres \r\n
        linea = mensaje[:-2]

        # lo invertimos
        linea = linea[::-1]

        # añadimos \r\n y enviamos
        respuesta = linea + "\r\n"

        sd.sendall(respuesta.encode("utf-8"))

    sd.close()