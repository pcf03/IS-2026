import socket
import sys

# 1. Configurar IP y puerto del servidor desde la terminal[cite: 13, 19]
ip = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
puerto = int(sys.argv[2]) if len(sys.argv) > 2 else 9999

# 2. Crear el socket UDP para el cliente[cite: 14]
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 3. Establecer un tiempo límite de espera (timeout) de 0.1 segundos para recibir respuesta[cite: 10, 11]
s.settimeout(0.1)

# 4. Inicializar el contador para numerar cada mensaje[cite: 9]
contador = 1

while True:
    # 5. Pedir texto por teclado al usuario
    mensaje = input("Introduce un texto (o FIN para salir): ")
    if mensaje == "FIN":
        break
        
    # 6. Formatear el mensaje con el número y enviarlo codificado en bytes[cite: 9, 18]
    mensaje_numerado = f"{contador}: {mensaje}"
    s.sendto(mensaje_numerado.encode("utf-8"), (ip, puerto))
    
    # 7. Usamos un bloque try/except para controlar el límite de tiempo[cite: 11]
    try:
        # Intentamos recibir la confirmación del servidor (se pausa aquí máximo 0.1s)[cite: 10, 11]
        confirmacion, origen_respuesta = s.recvfrom(1024)
        
        # Si llega algo, comprobamos que el contenido sea "OK"[cite: 11]
        if confirmacion.decode("utf-8") == "OK":
            print("Confirmación recibida: OK")
            
    except socket.timeout:
        # 8. Si pasan los 0.1s de límite sin respuesta, Python lanza el error socket.timeout y se ejecuta esto[cite: 11]
        print("ERROR. El datagrama de confirmación no llega")
        
    # 9. Incrementar el contador para el siguiente mensaje[cite: 9]
    contador += 1