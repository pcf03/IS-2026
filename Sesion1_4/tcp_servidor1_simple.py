import socket
import sys

# Puerto por defecto 9999 si no se especifica
puerto = int(sys.argv[1]) if len(sys.argv) > 1 else 9999

# Crear socket TCP[cite: 3]
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", puerto))
s.listen(5) # Modo pasivo[cite: 3]

while True:
    print(f"Esperando cliente en puerto {puerto}...")
    sd, origen = s.accept()

    continuar = True
    while continuar:
        datos_bytes = sd.recv(5) # Leemos exactamente 5 bytes[cite: 3]
        datos = datos_bytes.decode("ascii")

        if datos == "": # El cliente cerró la conexión[cite: 3]
            sd.close()
            continuar = False
        elif datos == "FINAL":
            print("Recibido FINAL")
            sd.close()
            continuar = False
        else:
            print(f"Recibido: {datos}")