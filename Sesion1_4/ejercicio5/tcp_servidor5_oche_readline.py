import socket
import sys
import time

puerto = int(sys.argv[1]) if len(sys.argv) > 1 else 9999
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", puerto))
s.listen(5)

while True:
    print(f"Servidor 'readline' esperando cliente en puerto {puerto}...")
    sd, origen = s.accept()
    time.sleep(1)
    
    # "Convertimos" el socket en un fichero configurando su codificación y salto de línea
    f = sd.makefile(encoding="utf8", newline="\r\n")
    
    while True:
        # Leemos hasta el \r\n (y lo incluye al final)[cite: 11, 12]
        mensaje = f.readline()
        
        if not mensaje: # Si llega vacío, el cliente cerró
            break
            
        linea = mensaje[:-2] # Quitamos el \r\n[cite: 8]
        linea_invertida = linea[::-1]
        
        # Para enviar, seguimos usando el socket normal, así que hay que codificar a bytes[cite: 8]
        sd.sendall((linea_invertida + "\r\n").encode("utf8"))
        
    f.close()
    sd.close()