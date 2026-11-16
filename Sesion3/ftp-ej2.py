import ftplib
import getpass

user = input("Introduce tu usuario (ej. alumno): ")
clave = getpass.getpass("Clave? ")

f = ftplib.FTP("localhost")
f.login(user, clave)

carpeta = input("Introduce la carpeta remota a listar: ")
f.cwd(carpeta)

print("\n--- Ficheros encontrados (filtrando directorios especiales) ---")
# MLSD devuelve tuplas (nombre, metadatos) por cada elemento
for nombre, meta in f.mlsd():
    # Omitir pseudo-carpetas cdir y pdir
    if "type" in meta and meta["type"] in ("cdir", "pdir"):
        continue
    # Mostrar solo el nombre del fichero o subcarpeta regular
    if meta.get("type") == "file":
        print(f"[Archivo] {nombre}")
    elif meta.get("type") == "dir":
        print(f"[Carpeta] {nombre}")

f.quit()