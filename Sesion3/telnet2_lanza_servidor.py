import telnetlib
import getpass
import time

HOST = "localhost"
user = input("Introduce tu usuario (ej. alumno): ")
password = getpass.getpass("Introduce tu contraseña: ")

tn = telnetlib.Telnet(HOST)

tn.read_until(b"login: ")
tn.write(user.encode('utf-8') + b"\n")

tn.read_until(b"Password: ")
tn.write(password.encode('utf-8') + b"\n")

tn.read_until(b"$")
tn.write(b"ps -ef\n")

salida_ps = tn.read_until(b"$").decode('utf-8')

if "udp_servidor3_con_ok.py" in salida_ps:
    print("\nEl servidor ya está en ejecución.")
else:
    print("\nEl servidor no está en ejecución. Lanzando...")
    tn.write(b"nohup python3 udp_servidor3_con_ok.py &\n")
    tn.read_until(b"$")
    time.sleep(1)

tn.write(b"exit\n")
tn.read_all()