"""Smtp client services module"""

import socket
import ssl
import base64


class SmtpClientOption:
    """smtp client options class"""

    def __init__(
        self,
        smtp_server: str = "",
        smtp_port: int = 25,
        secure: bool = False,
        username: str = "",
        password: str = "",
    ):
        self.smtp_server: str = smtp_server
        self.smtp_port: int = smtp_port
        self.secure: bool = secure
        self.username: str = username
        self.password: str = password


class SmtpClientServices:
    """Implements some mail services from a smtp client"""

    def __init__(self, options: SmtpClientOption):
        self.smtp_server: str = options.smtp_server
        self.smtp_port: int = options.smtp_port
        self.secure: bool = options.secure
        self.username: str = options.username
        self.password: str = options.password

    def send_mail(
        self,
        sender_mail: str,
        receiver_mail: str,
        subject: str,
        body: str,
        attachments_files: str = "",
    ):
        """Send an email using the Simple Mail Transfer Protocol (SMTP)"""
        with socket.socket(
            family=socket.AF_INET, type=socket.SOCK_STREAM
        ) as client_socket:
            try:
                client_socket.connect((self.smtp_server, self.smtp_port))

                # print the welcome message
                print(client_socket.recv(1024).decode())

                # send the EHLO command
                client_socket.sendall(b"EHLO\r\n")
                print(client_socket.recv(1024).decode())

                if self.secure:

                    # send the starttls command
                    client_socket.sendall(b"STARTTLS\r\n")
                    print(client_socket.recv(1024).decode())

                    # wrap the socket with ssl
                    context = ssl.SSLContext(protocol=ssl.PROTOCOL_TLSv1_2)
                    client_socket = context.wrap_socket(
                        client_socket,
                        server_hostname=self.smtp_server,
                    )
                #
                # AUTHENTICATION
                #

                client_socket.sendall("AUTH LOGIN\r\n".encode())
                print(client_socket.recv(1024).decode())

                # Enviar nombre de usuario codificado en base64
                user_base64 = base64.b64encode(self.username.encode()).decode() + "\r\n"
                client_socket.sendall(user_base64.encode())
                print(client_socket.recv(1024).decode())

                # Enviar contraseña codificada en base64
                pass_base64 = base64.b64encode(self.password.encode()).decode() + "\r\n"
                client_socket.sendall(pass_base64.encode())
                print(client_socket.recv(1024).decode())

                #
                # SEND EMAIL COMMANDS
                #

                # send the sender mail
                client_socket.sendall(f"MAIL FROM: <{sender_mail}>\r\n".encode())
                print(client_socket.recv(1024).decode())

                # Send the receiver mail
                client_socket.sendall(f"RCPT TO: <{receiver_mail}>\r\n".encode())
                print(client_socket.recv(1024).decode())

                # Send the data command
                client_socket.sendall(b"DATA\r\n")
                print(client_socket.recv(1024).decode())

                # send the encoded data
                msg_body = f"Subject: {subject}\r\nFrom: {sender_mail}\r\nTo: {receiver_mail}\r\n\r\n{body}\r\n.\r\n"
                msg_body += attachments_files
                client_socket.sendall(msg_body.encode())
                print(client_socket.recv(1024).decode())

                # send the quit commnad to close the connection
                client_socket.sendall(b"QUIT\r\n")
                print(client_socket.recv(1024).decode())

            except socket.error as sock_error:
                print(sock_error)
                return sock_error
