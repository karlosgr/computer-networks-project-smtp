"""a test module"""

import src.services.mail_services as mls


client_options = mls.SmtpClientOption(
    "localhost", 2525, secure=True, username="karlos", password="1234"
)

client = mls.SmtpClientServices(client_options)

client.send_mail("pedrito@ju", "Pedir@lo", "marito", "askjdkasjd")
