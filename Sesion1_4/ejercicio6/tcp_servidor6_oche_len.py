import socket
import sys

puerto = int(sys.argv[1]) if len(sys.argv) > 1 else 9999
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", puerto))
s.listen(5)

while True:
    print(f"Servidor leyendo longitudes esperando en puerto {puerto}...")
    sd, origen = s.accept()
    
    # Creamos el fichero asociado al socket para aprovechar sus buffers
    f = sd.makefile(encoding="utf8")
    
    while True:
        # 1. Leemos la línea inicial que contiene solo el número y el \n
        linea_longitud = f.readline()
        if not linea_longitud:
            break
            
        # Convertimos a entero (la función int() ignora automáticamente el \n)[cite: 13]
        longitud = int(linea_longitud)
        
        # 2. Leemos exactamente los caracteres que nos indica la longitud[cite: 13]
        mensaje = f.read(longitud)
        
        # 3. Le damos la vuelta. Ya no hay que preocuparse de quitar separadores \r\n
        mensaje_invertido = mensaje[::-1]
        
        # 4. Preparamos la respuesta: calculamos su longitud, le pegamos un \n y el texto[cite: 13]
        longitud_resp = f"{len(mensaje_invertido.encode('utf8'))}\n"
        
        # Enviamos todo junto de vuelta al cliente[cite: 13]
        sd.sendall((longitud_resp + mensaje_invertido).encode("utf8"))
        
    f.close()
    sd.close()