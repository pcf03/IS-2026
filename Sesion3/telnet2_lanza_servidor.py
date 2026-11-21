import telnetlib
import getpass

HOST = "localhost"
user = input("Introduce tu usuario (ej. alumno): ")
password = getpass.getpass("Introduce tu contraseña: ")

# 1. Conexión Telnet con el servidor remoto
tn = telnetlib.Telnet(HOST)

tn.read_until(b"login: ")
tn.write(user.encode('utf-8') + b"\n")

tn.read_until(b"Password: ")
tn.write(password.encode('utf-8') + b"\n")

tn.read_until(b"$")

# 2. Consultamos todos los contenedores (docker ps -a) mostrando solo nombre y estado
tn.write(b'docker ps -a --format "{{.Names}}|{{.Status}}"\n')
salida_docker = tn.read_until(b"$").decode('utf-8')

# 3. Nos desconectamos
tn.write(b"exit\n")
tn.read_all()
tn.close()

# 4. Identificamos los contenedores que NO están en ejecución (estado distinto de "Up")
print("\nContenedores detenidos en el servidor remoto:")
print("-" * 50)

detenidos = 0
for linea in salida_docker.splitlines():
    linea = linea.strip()
    # Ignoramos el eco del comando y las líneas sin datos
    if "|" not in linea or "docker ps" in linea:
        continue
    nombre, estado = linea.split("|", 1)
    if not estado.startswith("Up"):
        print(f"Nombre: {nombre:<25} Estado: {estado}")
        detenidos += 1

if detenidos == 0:
    print("No hay contenedores detenidos.")