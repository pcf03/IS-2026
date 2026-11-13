import socket
import sys
import random

ip = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
puerto = int(sys.argv[2]) if len(sys.argv) > 2 else 9999

# Crear el socket UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 1. Usar connect para fijar el origen y descartar paquetes de otras IPs automáticamente
s.connect((ip, puerto))

while True:
    mensaje = input("Introduce un texto (o FIN para salir): ")
    if mensaje == "FIN":
        break
        
    # 2. Generar un identificador aleatorio único para este mensaje
    id_msg = str(random.randint(10000, 99999))
    mensaje_numerado = f"{id_msg}:{mensaje}"
    datos_a_enviar = mensaje_numerado.encode("utf-8")
    
    timeout_actual = 0.1
    exito = False
    
    while timeout_actual <= 2.0:
        s.settimeout(timeout_actual)
        
        # Al usar connect, usamos send() en lugar de sendto()
        s.send(datos_a_enviar)
        
        try:
            # Al usar connect, usamos recv() y el SO filtra por la IP/Puerto
            confirmacion = s.recv(1024).decode("utf-8")
            
            # 3. Comprobar que la confirmación es exactamente para nuestro ID
            if confirmacion == f"OK:{id_msg}":
                print(f"Confirmación recibida: OK para el mensaje con ID {id_msg}")
                exito = True
                break
            else:
                print("Confirmación ignorada (no coincide el ID)")
                
        except socket.timeout:
            print(f"Timeout de {timeout_actual}s agotado. Reintentando...")
            timeout_actual *= 2
            
    if not exito:
        print("Puede que el servidor esté caído. Inténtelo más tarde")
        sys.exit(1)