import paramiko
import getpass

host = "localhost"
user = input("Introduce tu usuario (ej. alumno): ")
password = getpass.getpass("Introduce tu contraseña: ")

# 1. Crear cliente SSH y conectar
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username=user, password=password)

# 2. Abrir canal SFTP sobre la conexión SSH existente
sftp = client.open_sftp()

print("\n--- Listado de la carpeta home remota ---")
# 3. Listar contenidos de la carpeta por defecto del usuario
listado = sftp.listdir()
for nombre in listado:
    print(nombre)

# 4. Cerrar canales
sftp.close()
client.close()