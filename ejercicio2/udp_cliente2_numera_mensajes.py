import socket
import sys

# Obtener IP y puerto del servidor por argumentos o usar valores por defecto
servidor_ip = sys.argv[1] if len(sys.argv) > 1 else "localhost"
servidor_puerto = int(sys.argv[2]) if len(sys.argv) > 2 else 9999

# Crear el socket UDP del cliente
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print(f"Conectando con el servidor {servidor_ip}:{servidor_puerto}. Escribe 'FIN' para salir.")

# Inicializar el contador de mensajes
contador = 1

# Bucle para leer del teclado y enviar
while True:
    texto = input("Mensaje a enviar: ")

    # Formatear el mensaje añadiendo el número secuencial al principio
    mensaje_numerado = f"{contador}: {texto}"
    
    # Enviar convertido a bytes usando encode("utf-8")
    s.sendto(mensaje_numerado.encode("utf-8"), (servidor_ip, servidor_puerto))

    # Incrementar el contador para el siguiente datagrama
    contador += 1
    
    if texto == "FIN":
        break