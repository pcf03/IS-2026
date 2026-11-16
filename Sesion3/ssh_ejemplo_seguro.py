import paramiko
import base64
import getpass

user = input("Introduce tu usuario (ej. alumno): ")
password = getpass.getpass("Introduce tu contraseña: ")

client = paramiko.SSHClient()
# Por defecto se usa RejectPolicy (rechaza si no conoce la clave)

# Registramos explícitamente la clave pública ed25519 del servidor
clave_b64 = b"AAAAC3NzaC1lZDI1NTE5AAAAIHtrPHcZuD4uSTiwQO9Rs1hY25LhG0Y+e4xzf9b8Q8FM"
key = paramiko.Ed25519Key(data=base64.b64decode(clave_b64))
client.get_host_keys().add('localhost', 'ssh-ed25519', key)

client.connect('localhost', username=user, password=password)
print("¡Conexión SSH 100% segura y verificada!")

stdin, stdout, stderr = client.exec_command('ls')
print("\n--- SALIDA ---")
for line in stdout:
    print(line.rstrip())

client.close()