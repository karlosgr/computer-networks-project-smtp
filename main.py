"""this is the main file of the app"""

import flet as ft
import src.screens.mail_page as mail
import src.screens.config_page as config
import src.services.mail_services as ems


def main(page: ft.Page):
    """flet main page"""
    page.title = "SMTP Client"
    page.scroll = True
    page.bgcolor = "white"
    page.fonts = {
        "Poppins": "assets/fonts/Poppins-Regular.ttf",
    }

    def config_page(_=None):
        page.clean()
        config.config_page(page, function=mail_page)

    def mail_page(
        options: ems.SmtpClientOption,
        _=None,
    ):
        page.clean()
        mail.mail_page(page, options=options, function=config_page)

    config_page()


ft.app(main)
