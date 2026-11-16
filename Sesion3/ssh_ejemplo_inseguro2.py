import paramiko
import getpass

user = input("Introduce tu usuario (ej. alumno): ")
password = getpass.getpass("Introduce tu contraseña: ")

client = paramiko.SSHClient()

# Política que acepta la clave pero muestra un aviso (warning)
client.set_missing_host_key_policy(paramiko.WarningPolicy())

client.connect('localhost', username=user, password=password)
print("¡Conectado con WarningPolicy!")

stdin, stdout, stderr = client.exec_command('ls')

print("\n--- SALIDA DEL COMANDO ---")
for line in stdout:
    print(line.rstrip())

client.close()