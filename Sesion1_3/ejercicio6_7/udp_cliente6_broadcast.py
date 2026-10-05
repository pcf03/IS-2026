import socket

# Creamos el socket UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Activamos el modo Broadcast para poder "gritar" a toda la red
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

# Ponemos un límite de 2 segundos para no esperar respuestas para siempre
s.settimeout(2.0)

# La IP especial '<broadcast>' envía el paquete a TODOS los equipos conectados
print("Buscando servidores en la red...")
s.sendto(b"BUSCANDO HOLA", ("<broadcast>", 12345))

servidor_encontrado = None

# Bucle para escuchar a todos los servidores que vayan respondiendo
while True:
    try:
        datagrama, origen = s.recvfrom(1024)
        if datagrama.decode("utf-8") == "IMPLEMENTO HOLA":
            print(f"Servidor encontrado: {origen[0]}")
            # Guardamos la IP del PRIMER servidor que responda
            if servidor_encontrado is None:
                servidor_encontrado = origen[0]
    except socket.timeout:
        # Si pasan 2 segundos sin más respuestas, salimos del bucle
        break

# Si logramos encontrar al menos un servidor en la red...
if servidor_encontrado:
    print(f"Saludando al primer servidor: {servidor_encontrado}...")
    # Aquí ya NO usamos broadcast, enviamos el saludo directo a su IP concreta
    s.sendto(b"HOLA", (servidor_encontrado, 12345))
    
    try:
        # Esperamos su respuesta personalizada
        respuesta, _ = s.recvfrom(1024)
        print(f"Respuesta final: {respuesta.decode('utf-8')}")
    except socket.timeout:
        print("El servidor no respondió al saludo final.")
else:
    print("No hay servidores en la red.")