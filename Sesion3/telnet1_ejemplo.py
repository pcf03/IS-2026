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

tn.write(b"ls /home\n")
tn.write(b"exit\n")

print(tn.read_all().decode('utf-8'))