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

    # este es el tiempo max de espera
    timeout = 0.1

    # indica si el servidor confirma el datagrama
    confirmado = False

    # esperamos mientras el timeout no supere 2 seg
    # y mientras no hayamos recibido el OK
    while timeout <= 2 and not confirmado:

        # enviamos o reenviamos el mismo datagrama
        cliente.sendto(datagrama.encode("utf-8"), (ip, puerto))

        print("Enviado:", datagrama)
        print("Timeout:", timeout)

        # esperamos como max el tiempo indicado
        cliente.settimeout(timeout)

        try:
            respuesta, origen = cliente.recvfrom(1024)
            respuesta = respuesta.decode("utf-8")

            if respuesta == "OK":
                print("Recibida confirmación")
                confirmado = True
            else:
                print("Recibido datagrama no esperado")

        except socket.timeout:
            # no llega la confirmacion en el tiempo esperado
            print("No se ha recibido confirmación")
            # duplicamos tiempo para el siguiente intento
            timeout = timeout * 2

    # si salimos del bucle sin recibir OK
    # asumimos que el servidor puedo estar caido
    if not confirmado:
        print("Puede que el servidor esté caído. Inténtelo más tarde")
        break

    # incrementamos si el datagrama ha sido confirmado
    contador += 1

cliente.close()