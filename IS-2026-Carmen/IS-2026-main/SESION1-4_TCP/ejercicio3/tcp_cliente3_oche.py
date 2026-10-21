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

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# establecemos conexion con el servidor
cliente.connect((ip, puerto))

# mensajes a probar
mensajes = ["HOLA", "MUNDO", "PYTHON"]
# enviamos los 5 ABCDE
for mensaje in mensajes:

    # añadimos el delimitador de fin de mensaje
    mensaje = mensaje + "\r\n"

    # enviamos mensaje completo
    cliente.sendall(mensaje.encode("utf-8"))

    respuesta = cliente.recv(80)
    respuesta = respuesta.decode("utf-8")

    print("Respuesta: ", respuesta)

cliente.close()