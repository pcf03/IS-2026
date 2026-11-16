import ftplib
import getpass

user = input("Introduce tu usuario (ej. alumno): ")
clave = getpass.getpass("Clave? ")

# 1. Conectar al servidor FTP local
f = ftplib.FTP("localhost")
f.login(user, clave)

# 2. Entrar en la carpeta 'prueba' (Opción 2)
try:
    f.cwd("prueba")
    print("Directorio cambiado a 'prueba' con éxito.")
except Exception as e:
    print(f"Error al cambiar de directorio: {e}")

fichero_remoto = "prueba.txt"
fichero_local = "prueba-copia.txt"

# 3. Abrir fichero local en modo binario ("wb") y descargar
with open(fichero_local, "wb") as f_local:
    result = f.retrbinary(f"RETR {fichero_remoto}", f_local.write)

print("Resultado de la transferencia:", result)
print(f"Fichero descargado con éxito como '{fichero_local}'.")

f.quit()