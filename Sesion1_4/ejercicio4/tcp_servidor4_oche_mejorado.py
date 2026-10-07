import socket
import sys
import time

def recibe_mensaje(sock):
    buffer = [] # Usamos una lista de bytes por eficiencia
    while True:
        # Leemos los bytes de uno en uno[cite: 10]
        byte = sock.recv(1)
        if not byte:
            return b"" # El cliente cerró la conexión
        
        buffer.append(byte) # Añadimos el byte a la lista
        
        # Si el byte leído es el salto de línea, hemos terminado el mensaje[cite: 10]
        if byte == b"\n":
            break
            
    # Unimos todos los bytes de la lista en una sola cadena de bytes[cite: 11]
    return b"".join(buffer)

puerto = int(sys.argv[1]) if len(sys.argv) > 1 else 9999
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", puerto))
s.listen(5)

while True:
    print(f"Servidor mejorado esperando cliente en puerto {puerto}...")
    sd, origen = s.accept()
    
    # Mantenemos el retardo para forzar que los mensajes se amontonen[cite: 11]
    time.sleep(1)
    
    while True:
        # Usamos nuestra nueva función a prueba de fallos[cite: 11]
        mensaje_bytes = recibe_mensaje(sd)
        if not mensaje_bytes:
            break
            
        mensaje = mensaje_bytes.decode("utf8")
        linea = mensaje[:-2] # Quitamos el \r\n final
        linea_invertida = linea[::-1]
        
        # Enviamos la respuesta con su \r\n[cite: 8]
        sd.sendall((linea_invertida + "\r\n").encode("utf8"))
        
    sd.close()