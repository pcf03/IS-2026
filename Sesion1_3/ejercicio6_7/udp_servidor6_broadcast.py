import socket

# Creamos el socket UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Activamos la opción especial para permitir escuchar mensajes Broadcast
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

# Nos quedamos escuchando en el puerto fijo 12345
s.bind(("", 12345))

print("Servidor escuchando a toda la red en el puerto 12345...")

while True:
    # Esperamos a que nos llegue un mensaje de cualquier cliente
    datagrama, origen = s.recvfrom(1024)
    texto = datagrama.decode("utf-8")
    
    # Si alguien grita preguntando quién tiene el servicio...
    if texto == "BUSCANDO HOLA":
        print(f"Petición de {origen[0]}")
        # Le respondemos diciendo "¡Yo lo tengo!"
        s.sendto(b"IMPLEMENTO HOLA", origen)
        
    # Si el cliente ya nos ha elegido y nos manda el saludo final...
    elif texto == "HOLA":
        print(f"Saludo de {origen[0]}")
        # Le devolvemos un mensaje que incluye su propia IP
        respuesta = f"HOLA: {origen[0]}"
        s.sendto(respuesta.encode("utf-8"), origen)