import socket
import sys

# 1. Configurar IP y puerto del servidor desde los argumentos de la terminal
ip = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
puerto = int(sys.argv[2]) if len(sys.argv) > 2 else 9999

# 2. Crear el socket UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 3. Inicializar el contador para el número de secuencia de los datagramas
contador = 1

while True:
    # 4. Pedir al usuario el texto a enviar
    mensaje = input("Introduce un texto (o FIN para salir): ")
    if mensaje == "FIN":
        break
        
    # 5. Añadir el número de secuencia al mensaje y codificarlo a bytes[cite: 8, 10]
    mensaje_numerado = f"{contador}: {mensaje}"
    datos_a_enviar = mensaje_numerado.encode("utf-8")
    
    # 6. Variables para controlar el bucle de reintentos
    timeout_actual = 0.1  # Empezamos con un tiempo de espera de 0.1 segundos
    exito = False         # Bandera para saber si logramos recibir el OK
    
    # 7. Bucle de reintentos: se repite mientras el timeout no supere los 2 segundos[cite: 10]
    while timeout_actual <= 2.0:
        
        # Aplicar el tiempo de espera actual al socket[cite: 10]
        s.settimeout(timeout_actual)
        
        # Enviar (o reenviar) el datagrama al servidor[cite: 10]
        s.sendto(datos_a_enviar, (ip, puerto))
        
        try:
            # Esperar la respuesta (se bloqueará como máximo el tiempo de timeout_actual)
            confirmacion, origen_respuesta = s.recvfrom(1024)
            
            if confirmacion.decode("utf-8") == "OK":
                print("Confirmación recibida: OK")
                exito = True  # Marcamos que el envío fue exitoso
                break         # Salimos del bucle de reintentos para pedir el siguiente mensaje[cite: 10]
                
        except socket.timeout:
            # Si expira el tiempo, informamos por pantalla y preparamos el reintento
            print(f"Timeout de {timeout_actual}s agotado. Reintentando...")
            
            # Duplicar el valor del timeout para el próximo reenvío (0.1 -> 0.2 -> 0.4 -> 0.8 -> 1.6)[cite: 10]
            timeout_actual *= 2
            
    # 8. Comprobar qué ocurrió al salir del bucle de reintentos
    if not exito:
        # Si salimos del bucle y exito sigue siendo False, superamos los 2 segundos sin respuesta[cite: 10]
        print("Puede que el servidor esté caído. Inténtelo más tarde")
        sys.exit(1)  # Finalizar la ejecución del programa indicando un error[cite: 10]
        
    # 9. Incrementar el número de secuencia SOLO si el mensaje llegó con éxito[cite: 10]
    # Si hubo reintentos, el número se mantuvo igual como pide el enunciado
    contador += 1