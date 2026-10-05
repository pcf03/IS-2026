import socket
import sys
import random

# 1. Configurar el puerto desde argumentos de terminal o usar el 9999 por defecto[cite: 13, 19]
puerto = int(sys.argv[1]) if len(sys.argv) > 1 else 9999

# 2. Crear el socket UDP y asignarle el puerto para escuchar peticiones[cite: 14]
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("", puerto))

print(f"Servidor con OK escuchando en el puerto {puerto}...")

while True:
    # 3. Esperar a recibir un datagrama del cliente[cite: 16]
    datagrama, origen = s.recvfrom(1024)
    
    # 4. Simular pérdida de paquetes de la red (50% de probabilidad)[cite: 9]
    if random.randint(0, 1) == 0:
        print("Simulando paquete perdido")
    else:
        # 5. Si el paquete no se ha perdido, decodificarlo y mostrarlo por pantalla[cite: 9, 10]
        texto = datagrama.decode("utf-8")
        print(f"Recibido de {origen}: {texto}")
        
        # 6. Enviar confirmación de vuelta al cliente. 
        # La 'b' delante de "OK" lo convierte directamente en cadena de bytes[cite: 5, 10]
        s.sendto(b"OK", origen)