import telnetlib
import getpass

HOST = "localhost"
user = input("Introduce tu usuario (ej. alumno): ")
password = getpass.getpass("Introduce tu contraseña: ")

tn = telnetlib.Telnet(HOST)

tn.read_until(b"login: ")
tn.write(user.encode('utf-8') + b"\n")

tn.read_until(b"Password: ")
tn.write(password.encode('utf-8') + b"\n")

# Leer y descartar todo hasta el primer prompt
tn.read_until(b"$")

tn.write(b"ls /home\n")

# Capturar solo la salida del comando
salida = tn.read_until(b"$").decode('utf-8')
print("\n--- SALIDA LIMPIA ---")
print(salida)

tn.write(b"exit\n")
tn.read_all()