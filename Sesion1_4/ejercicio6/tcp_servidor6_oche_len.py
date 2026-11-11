import socket
import sys

puerto = int(sys.argv[1]) if len(sys.argv) > 1 else 9999
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", puerto))
s.listen(5)

while True:
    print(f"Servidor leyendo longitudes esperando en puerto {puerto}...")
    sd, origen = s.accept()
    
    f = sd.makefile(encoding="utf8", newline="\n")
    
    while True:
        # 1. Leemos la línea inicial que contiene la longitud y el \n
        linea_longitud = f.readline()
        if not linea_longitud:
            break
            
        # Convertimos a entero
        longitud = int(linea_longitud)
        
        # 2. Leemos exactamente los caracteres que nos indica la longitud
        mensaje = f.read(longitud)
        
        # 3. Le damos la vuelta
        mensaje_invertido = mensaje[::-1]
        
        # 4. Preparamos la respuesta: calculamos longitud, \n y texto
        mensaje_invertido_bytes = mensaje_invertido.encode("utf8")
        longitud_resp = f"{len(mensaje_invertido_bytes)}\n"
        
        # Enviamos todo junto al cliente usando sendall sobre el socket
        sd.sendall(longitud_resp.encode("utf8") + mensaje_invertido_bytes)
        
    f.close()
    sd.close()