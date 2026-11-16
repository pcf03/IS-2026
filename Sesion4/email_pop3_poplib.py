import poplib
import os
import sys

# Leer credenciales desde las variables de entorno
username = os.environ.get("GMAIL_USER")
password = os.environ.get("GMAIL_APP_PASSWORD")

if not username or not password:
    print("ERROR: Faltan las variables de entorno GMAIL_USER o GMAIL_APP_PASSWORD.")
    sys.exit(1)

server = "pop.gmail.com"

print(f"Conectando a {server} usando poplib con SSL...")
# Instanciar el objeto POP3 con SSL y activar la depuración
pop3_mail = poplib.POP3_SSL(server)
pop3_mail.set_debuglevel(2)

# Autenticación con user() y pass_()
print("Autenticando...")
pop3_mail.user(username)
pop3_mail.pass_(password)

# Obtener estadísticas del buzón (STAT)
num_msgs, total_size = pop3_mail.stat()
print(f"\n--- ESTADÍSTICAS DEL BUZÓN ---")
print(f"Número de mensajes: {num_msgs}")
print(f"Tamaño total: {total_size} bytes")

if num_msgs > 0:
    # Obtener el primer mensaje usando retr()
    # retr() retorna una tupla: (respuesta_servidor, lista_de_lineas_en_bytes, tamaño)
    print("\nDescargando el primer mensaje con retr(1)...")
    resp, mensaje_lineas, octets = pop3_mail.retr(1)
    
    print(f"Respuesta del servidor: {resp}")
    print(f"Tamaño del mensaje: {octets} bytes")
    
    print("\n--- PRIMERAS LÍNEAS DEL MENSAJE 1 ---")
    # Imprimimos las primeras 15 líneas de la lista
    for linea in mensaje_lineas[:15]:
        print(linea.decode("utf-8", errors="ignore"))

# Terminar la sesión
pop3_mail.quit()
print("\n¡Sesión POP3 con poplib cerrada con éxito!")