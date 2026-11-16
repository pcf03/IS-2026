import smtplib
import email.message
import email.utils
import os
import sys

# Leer credenciales desde las variables de entorno
username = os.environ.get("GMAIL_USER")
password = os.environ.get("GMAIL_APP_PASSWORD")

if not username or not password:
    print("ERROR: Faltan las variables de entorno GMAIL_USER o GMAIL_APP_PASSWORD.")
    sys.exit(1)

server = "smtp.gmail.com"
port = 587

fromaddr = username
toaddr = input("Introduce el correo de destino: ")

# Construir el mensaje cumpliendo el estándar RFC-5322
mensaje = email.message.EmailMessage()
mensaje['To'] = toaddr
mensaje['From'] = fromaddr
mensaje['Subject'] = 'Mensaje de prueba con smtplib y Gmail'
mensaje['Date'] = email.utils.formatdate(localtime=True)
mensaje['Message-ID'] = email.utils.make_msgid()
mensaje.set_content("Hola, este correo ha sido enviado utilizando la librería smtplib de Python y TLS.")

print(f"Conectando a {server}:{port} mediante smtplib...")
s = smtplib.SMTP(server, port)
s.set_debuglevel(1)

try:
    s.starttls()
    s.login(username, password)
    s.sendmail(fromaddr, toaddr, mensaje.as_bytes())
    print("¡Correo enviado con éxito usando smtplib!")
finally:
    s.quit()