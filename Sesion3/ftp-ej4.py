import ftplib
import getpass
import os

user = input("Introduce tu usuario (ej. alumno): ")
clave = getpass.getpass("Clave? ")

carpeta_remota = input("Introduce la carpeta remota de la que descargar todo: ")
carpeta_local = "./descargas_ftp_anexo"
os.makedirs(carpeta_local, exist_ok=True)

f = ftplib.FTP("localhost")
f.login(user, clave)
f.cwd(carpeta_remota)

print(f"\nDescargando contenido de la carpeta remota '{carpeta_remota}'...")

for nombre, meta in f.mlsd():
    # Omitir pseudo-carpetas y directorios (solo descargar ficheros regulares)
    if meta.get("type") == "file":
        ruta_local = os.path.join(carpeta_local, nombre)
        print(f"Descargando: {nombre} -> {ruta_local}")
        
        with open(ruta_local, "wb") as f_local:
            f.retrbinary(f"RETR {nombre}", f_local.write)

print("\n¡Descarga masiva FTP completada!")
f.quit()