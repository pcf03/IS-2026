import getpass
import telnetlib

HOST = "localhost"
# Pedimos las credenciales al usuario[cite: 23]
user = input("Introduce tu usuario (ej. uo287992): ")
password = getpass.getpass("Introduce tu contraseña: ")

# Iniciamos la conexión[cite: 23]
tn = telnetlib.Telnet(HOST)

# Esperamos a que el servidor pida el login y lo enviamos
tn.read_until(b"login: ")
tn.write(user.encode('utf-8') + b"\n")

# Esperamos a que pida la contraseña y la enviamos[cite: 24]
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('utf-8') + b"\n")

# El truco: leemos y descartamos todo hasta encontrar el símbolo "$" del prompt[cite: 24]
tn.read_until(b"$")

# Ahora que el shell está listo, enviamos el comando para listar /home[cite: 23]
tn.write(b"ls /home\n")

# Cerramos la sesión[cite: 24]
tn.write(b"exit\n")

# Leemos toda la respuesta restante hasta que se cierre el socket y la decodificamos en UTF-8[cite: 23, 24]
respuesta = tn.read_all()
print("\n--- SALIDA DEL COMANDO ---")
print(respuesta.decode('utf-8'))