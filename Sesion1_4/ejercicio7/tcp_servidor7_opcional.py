import socket
import sys
import struct

def recvall(sock, count):
    buf = b''
    while len(buf) < count:
        newbuf = sock.recv(count - len(buf))
        if not newbuf: 
            return b''
        buf += newbuf
    return buf

puerto = int(sys.argv[1]) if len(sys.argv) > 1 else 9999
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", puerto))
s.listen(5)

while True:
    print(f"Servidor binario esperando en puerto {puerto}...")
    sd, origen = s.accept()
    
    while True:
        # 1. Leemos exactamente 2 bytes (la longitud codificada)[cite: 14, 15]
        len_bytes = recvall(sd, 2)
        if not len_bytes:
            break
            
        # 2. Desempaquetamos. unpack devuelve una tupla, nos quedamos con el primer elemento [0]
        longitud = struct.unpack(">H", len_bytes)[0]
        
        # 3. Leemos el resto del mensaje usando la longitud extraída[cite: 15]
        mensaje_bytes = recvall(sd, longitud)
        mensaje = mensaje_bytes.decode("utf8")
        
        # 4. Invertimos y preparamos la respuesta
        mensaje_invertido = mensaje[::-1]
        mensaje_invertido_bytes = mensaje_invertido.encode("utf8")
        
        # 5. Empaquetamos la nueva longitud y enviamos todo junto
        longitud_resp_bytes = struct.pack(">H", len(mensaje_invertido_bytes))
        sd.sendall(longitud_resp_bytes + mensaje_invertido_bytes)
        
    sd.close()