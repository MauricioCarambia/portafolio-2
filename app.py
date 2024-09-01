from flask import Flask, render_template, request, redirect, url_for
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['mail']
        asunto = request.form['asunto']
        consulta = request.form['consulta']

        # Configuración del correo
        destinatario = "mcarambia@gmail.com"  # Cambia esto a tu dirección de correo
        nombre = f"Consulta de {nombre}"
        asunto = f"Sobre {asunto}"
        mensaje = f"Nombre: {nombre}\nEmail: {email}\n\nConsulta:\n{consulta}"

        # Enviar correo
        enviar_correo(destinatario, nombre, asunto, mensaje, email)
        
        return "Consulta enviada con éxito."

    return render_template('formulario.html')

def enviar_correo(destinatario, asunto, mensaje, email):
    # Configuración del servidor SMTP
    servidor = 'smtp.gmail.com'  # Cambia esto al servidor SMTP de tu proveedor de correo
    puerto = 587
    usuario = 'mcarambia@gmail.com'  # Tu dirección de correo
    contraseña = 'esternocleidomastoideo195'  # Tu contraseña de correo

    msg = MIMEText(mensaje)
    msg['Subject'] = asunto
    msg['From'] = email
    msg['To'] = destinatario

    # Enviar el correo
    with smtplib.SMTP(servidor, puerto) as server:
        server.starttls()
        server.login(usuario, contraseña)
        server.sendmail(email, destinatario, msg.as_string())

if __name__ == '__main__':
    app.run(debug=True)
