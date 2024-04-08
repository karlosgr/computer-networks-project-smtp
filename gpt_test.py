import socket
import ssl
import base64

# Configuración del servidor SMTP y credenciales
smtp_server = (
    "localhost"  # Cambiar a la dirección IP o nombre de dominio del servidor SMTP
)
smtp_port = 2525  # Puerto SMTP estándar
smtp_username = "tu_usuario"  # Si el servidor SMTP requiere autenticación
smtp_password = "tu_contraseña"  # Si el servidor SMTP requiere autenticación

# Direcciones de correo electrónico
from_email = "from@example.com"
to_email = "to@example.com"

# Mensaje de correo electrónico
subject = "Prueba de correo electrónico"
body = "Hola,\n\nEste es un correo electrónico de prueba enviado desde Python."

# Establecer conexión con el servidor SMTP
try:
    smtp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    smtp_socket.connect((smtp_server, smtp_port))

    # Leer mensaje de bienvenida del servidor
    recv_data = smtp_socket.recv(1024)
    print(recv_data.decode())

    # Saludo inicial al servidor SMTP
    smtp_socket.sendall(b"EHLO example.com\r\n")
    recv_data = smtp_socket.recv(1024)
    print(recv_data.decode())

    # Iniciar cifrado TLS (opcional si el servidor lo soporta)
    smtp_socket.sendall(b"STARTTLS\r\n")
    recv_data = smtp_socket.recv(1024)
    print(recv_data.decode())

    # Establecer conexión cifrada
    smtp_socket = ssl.wrap_socket(smtp_socket)

    # Autenticación con el servidor SMTP (si es necesaria)
    if smtp_username and smtp_password:
        auth_msg = "AUTH LOGIN\r\n"
        smtp_socket.sendall(auth_msg.encode())
        recv_data = smtp_socket.recv(1024)
        print(recv_data.decode())

        # Enviar nombre de usuario codificado en base64
        user_base64 = base64.b64encode(smtp_username.encode()).decode() + "\r\n"
        smtp_socket.sendall(user_base64.encode())
        recv_data = smtp_socket.recv(1024)
        print(recv_data.decode())

        # Enviar contraseña codificada en base64
        pass_base64 = base64.b64encode(smtp_password.encode()).decode() + "\r\n"
        smtp_socket.sendall(pass_base64.encode())
        recv_data = smtp_socket.recv(1024)
        print(recv_data.decode())

    # Crear y enviar el mensaje de correo electrónico
    smtp_socket.sendall(f"MAIL FROM: <{from_email}>\r\n".encode())
    recv_data = smtp_socket.recv(1024)
    print(recv_data.decode())

    smtp_socket.sendall(f"RCPT TO: <{to_email}>\r\n".encode())
    recv_data = smtp_socket.recv(1024)
    print(recv_data.decode())

    smtp_socket.sendall(b"DATA\r\n")
    recv_data = smtp_socket.recv(1024)
    print(recv_data.decode())

    msg_body = f"Subject: {subject}\r\n\r\n{body}\r\n.\r\n"

    file = open("assets/icon.png", "rb").read()

    file_encoded = base64.b64encode(file).decode()

    msg_body += "Content-Type: application/octet-stream; name=icon.png\r\n"
    msg_body += "Content-Disposition: attachment; filename=icon.png\r\n"
    msg_body += "Content-Transfer-Encoding: base64\r\n"
    msg_body += f"\r\n{file_encoded}\r\n.\r\n"

    smtp_socket.sendall(msg_body.encode())
    recv_data = smtp_socket.recv(1024)
    print(recv_data.decode())

    # Cerrar conexión SMTP
    smtp_socket.sendall(b"QUIT\r\n")
    recv_data = smtp_socket.recv(1024)
    print(recv_data.decode())

    smtp_socket.close()
    print("Correo electrónico enviado con éxito!")
except Exception as e:
    print(f"Error al enviar el correo electrónico: {e}")
