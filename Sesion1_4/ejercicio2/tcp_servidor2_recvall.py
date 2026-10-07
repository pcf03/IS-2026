import socket
import sys

# Nueva función robusta para leer exactamente 'count' bytes
def recvall(sock, count):
    buf = b''
    while len(buf) < count:
        # Intentamos leer lo que nos falta para llegar a count
        newbuf = sock.recv(count - len(buf))
        if not newbuf: 
            return b'' # El cliente ha cerrado la conexión
        buf += newbuf
    return buf

puerto = int(sys.argv[1]) if len(sys.argv) > 1 else 9999
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", puerto))
s.listen(5)

while True:
    print(f"Esperando cliente en puerto {puerto}...")
    sd, origen = s.accept()
    
    continuar = True
    while continuar:
        # Usamos nuestra nueva función en lugar del recv() normal[cite: 5]
        datos_bytes = recvall(sd, 5)
        datos = datos_bytes.decode("ascii")

        if datos == "":
            sd.close()
            continuar = False
        elif datos == "FINAL":
            print("Recibido FINAL")
            sd.close()
            continuar = False
        else:
            print(f"Recibido: {datos}")