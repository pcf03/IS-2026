import ftplib
import getpass

# Callback para acumular las líneas recibidas
lista = []
def acumular(linea):
    lista.append(linea)

user = input("Introduce tu usuario (ej. alumno): ")
clave = getpass.getpass("Clave? ")

# 1. Conectar al servidor FTP local
f = ftplib.FTP("localhost")
f.login(user, clave)  # Envía comandos USER y PASS

# 2. Cambiar a la carpeta objetivo (debe existir)
carpeta = input("Introduce la carpeta remota a listar (ej. .): ")
f.cwd(carpeta)

# 3. Enviar comando LIST indicando el callback
lista = []
resp = f.retrlines("LIST", acumular)

print("Respuesta del protocolo:", resp)
print("\nContenidos de la carpeta remota:")
for l in lista:
    print(l)

f.quit()