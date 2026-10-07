import socket
import sys

ip = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
puerto = int(sys.argv[2]) if len(sys.argv) > 2 else 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, puerto))

# Lista de palabras a enviar al servidor
palabras = ["HOLA", "MUNDO", "REDES"]

for palabra in palabras:
    # Añadimos el delimitador al final de cada mensaje[cite: 7]
    mensaje_a_enviar = palabra + "\r\n"
    s.sendall(mensaje_a_enviar.encode("utf8"))
    
    # Recibimos la respuesta y la mostramos[cite: 8]
    respuesta_bytes = s.recv(80)
    respuesta = respuesta_bytes.decode("utf8")
    
    # Usamos strip() en el print para que no haga saltos de línea extra en la terminal
    print(f"Enviado: {palabra} -> Recibido: {respuesta.strip()}")

s.close()