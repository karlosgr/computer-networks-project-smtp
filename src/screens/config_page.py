"""This is the Home Page of the App"""

import flet as ft
import src.services.mail_services as emc

OPTIONS: emc.SmtpClientOption = emc.SmtpClientOption()


def config_page(page: ft.Page, function):
    """Home Page"""
    username = ""
    password = ""
    smtp_server = ""
    smtp_port = 25
    secure = False

    def on_username_change(event: ft.ControlEvent):
        nonlocal username
        username = str(event.control.value)

    def on_password_change(event: ft.ControlEvent):
        nonlocal password
        password = str(event.control.value)

    def on_smpt_server_change(event: ft.ControlEvent):
        nonlocal smtp_server
        smtp_server = str(event.control.value)

    def on_smtp_port_change(event: ft.ControlEvent):
        nonlocal smtp_port
        smtp_port = int(event.control.value)

    def on_secure_change(event: ft.ControlEvent):
        nonlocal secure
        secure = bool(event.control.value)

    def login_submit(_):
        OPTIONS.username = username
        OPTIONS.password = password
        OPTIONS.smtp_server = smtp_server
        OPTIONS.smtp_port = smtp_port
        OPTIONS.secure = secure
        function(options=OPTIONS)

    page.add(
        ft.SafeArea(
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Container(
                        height=30,
                    ),
                    ft.Text(
                        value="Config Client",
                        style=ft.TextStyle(
                            size=130,
                            color="blue",
                            font_family="Monsterrat",
                        ),
                        text_align=ft.TextAlign.CENTER,
                    ),
                    ft.Container(
                        height=60,
                    ),
                    ft.Container(
                        width=400,
                        content=ft.TextField(
                            value=OPTIONS.smtp_server,
                            label="SMPT Server",
                            focused_color="blue",
                            prefix_icon=ft.icons.NETWORK_CHECK,
                            cursor_color="black",
                            color=ft.colors.BLACK26,
                            on_change=on_smpt_server_change,
                        ),
                    ),
                    ft.Container(
                        height=20,
                    ),
                    ft.Container(
                        width=400,
                        content=ft.TextField(
                            value=OPTIONS.smtp_port,
                            label="SMTP Port",
                            focused_color="blue",
                            prefix_icon=ft.icons.NETWORK_PING,
                            cursor_color="black",
                            color=ft.colors.BLACK26,
                            on_change=on_smtp_port_change,
                        ),
                    ),
                    ft.Container(
                        height=20,
                    ),
                    ft.Container(
                        width=400,
                        content=ft.TextField(
                            value=OPTIONS.username,
                            label="User Name",
                            focused_color="blue",
                            prefix_icon=ft.icons.EMAIL_OUTLINED,
                            cursor_color="black",
                            color=ft.colors.BLACK26,
                            on_change=on_username_change,
                        ),
                    ),
                    ft.Container(
                        height=20,
                    ),
                    ft.Container(
                        width=400,
                        content=ft.TextField(
                            value=OPTIONS.password,
                            label="Password",
                            focused_color="blue",
                            prefix_icon=ft.icons.LOCK_OUTLINED,
                            cursor_color="black",
                            color=ft.colors.BLACK26,
                            password=True,
                            can_reveal_password=True,
                            on_change=on_password_change,
                        ),
                    ),
                    ft.Switch(
                        label="Secure Conection",
                        on_change=on_secure_change,
                        width=20,
                        value=OPTIONS.secure,
                    ),
                    ft.ElevatedButton(
                        bgcolor="blue",
                        width=400,
                        height=50,
                        content=ft.Text(
                            "Send Email !", style=ft.TextStyle(color="white", size=20)
                        ),
                        on_click=login_submit,
                    ),
                ],
            )
        )
    )
