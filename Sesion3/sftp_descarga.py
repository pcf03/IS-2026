import os
import paramiko
import getpass
from stat import S_ISDIR

host = "localhost"
user = input("Introduce tu usuario (ej. alumno): ")
password = getpass.getpass("Introduce tu contraseña: ")

carpeta_remota = input("Introduce la ruta de la carpeta remota a descargar (ej. /home/alumno): ")
carpeta_local = "./descargas_sftp"

# Crear carpeta local de destino si no existe
os.makedirs(carpeta_local, exist_ok=True)

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username=user, password=password)

# Abrir canal SFTP[cite: 29]
sftp = client.open_sftp()

print(f"\n--- Descargando archivos de '{carpeta_remota}' ---")
try:
    for nombre in sftp.listdir(carpeta_remota):
        ruta_remota = os.path.join(carpeta_remota, nombre).replace("\\", "/")
        
        try:
            # Obtener atributos del fichero remoto[cite: 30]
            attr = sftp.stat(ruta_remota)
            
            # Comprobar si es un directorio usando S_ISDIR[cite: 30]
            if S_ISDIR(attr.st_mode):
                print(f"[Omitido] '{nombre}' es un directorio.")
            else:
                ruta_local = os.path.join(carpeta_local, nombre)
                print(f"Descargando archivo regular: '{nombre}'...")
                # Descargar fichero remoto al equipo local[cite: 29]
                sftp.get(ruta_remota, ruta_local)
                
        except Exception as e:
            print(f"Error procesando '{nombre}': {e}")
            
except Exception as e:
    print(f"Error accediendo a la carpeta remota: {e}")

sftp.close()
client.close()
print("\n¡Proceso de descarga SFTP finalizado con éxito!")