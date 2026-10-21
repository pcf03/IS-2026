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

cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

contador = 1

while True:
    mensaje = input("Escribe un mensaje: ")

    if mensaje == "FIN":
        break

    datagrama = str(contador) + ": " + mensaje

    timeout = 0.1
    confirmado = False

    while timeout <= 2 and not confirmado:

        cliente.sendto(datagrama.encode("utf-8"), (ip, puerto))

        print("Enviado:", datagrama)
        print("Timeout:", timeout)

        cliente.settimeout(timeout)

        try:
            respuesta, origen = cliente.recvfrom(1024)
            respuesta = respuesta.decode("utf-8")

            # esta es la confirmacion que esperamos recibir
            confirmacion = "OK" + str(contador)

            # comprobamos qu eel OK coresponde al datagrama enviado
            if respuesta == confirmacion:
                print("Recibida confirmación", respuesta)
                confirmado = True
            else:
                print("Recibido datagrama no esperado", respuesta)

        except socket.timeout:
            print("No se ha recibido confirmación")
            timeout = timeout * 2

    if not confirmado:
        print("Puede que el servidor esté caído. Inténtelo más tarde")
        break

    contador += 1

cliente.close()