import socket
import sys
import random

puerto = int(sys.argv[1]) if len(sys.argv) > 1 else 9999
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("", puerto))

print(f"Servidor mejorado escuchando en el puerto {puerto}...")

# 1. Conjunto (set) para llevar registro de los identificadores procesados
mensajes_procesados = set()

while True:
    datagrama, origen = s.recvfrom(1024)
    
    # Simular pérdida de paquetes (50% de probabilidad)
    if random.randint(0, 1) == 0:
        print("Simulando paquete perdido")
        continue

    texto_recibido = datagrama.decode("utf-8")
    
    # Separar el ID del mensaje
    partes = texto_recibido.split(":", 1)
    if len(partes) != 2:
        continue # Ignorar si el formato no es ID:Mensaje
        
    id_msg, mensaje = partes
    
    # 2. Comprobar si el mensaje ya fue procesado antes (es un duplicado)
    if id_msg in mensajes_procesados:
        print(f"Mensaje {id_msg} duplicado. Reenviando confirmación sin reprocesar la acción.")
    else:
        print(f"Recibido de {origen}: {mensaje} (ID: {id_msg})")
        # Registrar como procesado para no repetir la acción en el futuro
        mensajes_procesados.add(id_msg)
    
    # 3. Enviar confirmación indicando explícitamente el ID que se está confirmando
    respuesta = f"OK:{id_msg}"
    s.sendto(respuesta.encode("utf-8"), origen)