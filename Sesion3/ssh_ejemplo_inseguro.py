import paramiko
import getpass

user = input("Introduce tu usuario (ej. alumno): ")
password = getpass.getpass("Introduce tu contraseña: ")

client = paramiko.SSHClient()

# Política para aceptar ciegamente la clave pública del servidor
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Conectar al servidor local
client.connect('localhost', username=user, password=password)
print("¡Conectado de forma segura por SSH!")

# Ejecutar un comando remoto (ls)
stdin, stdout, stderr = client.exec_command('ls')

# Mostrar el resultado línea a línea
print("\n--- SALIDA DEL COMANDO ---")
for line in stdout:
    print(line.rstrip())

client.close()