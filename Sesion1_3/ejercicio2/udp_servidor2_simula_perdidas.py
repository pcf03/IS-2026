import socket
import sys
import random

# Determinar el puerto (por línea de comandos o 9999 por defecto)
if len(sys.argv) > 1:
    puerto = int(sys.argv[1])
else:
    puerto = 9999

# Crear el socket UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Asociar el socket a cualquier IP local y al puerto elegido
s.bind(("", puerto))
print(f"Servidor UDP escuchando en el puerto {puerto}...")

# Bucle infinito para recibir datagramas
while True:
    datagrama, origen = s.recvfrom(1024)  # 1024 bytes máximo

    # Decidir aleatoriamente con un 50% de probabilidad (0 o 1)
    if random.randint(0, 1) == 0:
        print("Simulando paquete perdido")
    else:
        mensaje = datagrama.decode("utf-8")
        print(f"Recibido de {origen}: {mensaje}")