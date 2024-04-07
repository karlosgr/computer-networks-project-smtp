"""Smtp client services module"""

import socket
import ssl
import base64


class SmtpClientOption:
    """smtp client options class"""

    def __init__(
        self,
        smtp_server: str,
        smtp_port: int,
        secure: bool,
        username: str,
        password: str,
    ):
        self.smtp_server: str = smtp_server
        self.smtp_port: int = smtp_port
        self.secure: bool = secure
        self.username: str = username
        self.password: str = password

