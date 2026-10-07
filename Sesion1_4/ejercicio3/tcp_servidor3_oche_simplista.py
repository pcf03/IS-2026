import socket
import sys

puerto = int(sys.argv[1]) if len(sys.argv) > 1 else 9999
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", puerto))
s.listen(5)

while True:
    print(f"Servidor 'oche' esperando cliente en puerto {puerto}...")
    sd, origen = s.accept()
    
    while True:
        # 1. Recibir hasta 80 bytes y decodificar[cite: 7]
        mensaje_bytes = sd.recv(80)
        
        # Si devuelve vacío, el cliente ha cerrado la conexión
        if not mensaje_bytes:
            break 
            
        mensaje = mensaje_bytes.decode("utf8")
        
        # 2. Quitar el "fin de línea" (\r\n) cortando los 2 últimos caracteres
        linea = mensaje[:-2]
        
        # 3. Darle la vuelta al string usando el truco de los slices[cite: 7, 8]
        linea_invertida = linea[::-1]
        
        # 4. Enviar la respuesta añadiendo de nuevo el \r\n al final[cite: 8]
        sd.sendall((linea_invertida + "\r\n").encode("utf8"))
        
    sd.close()