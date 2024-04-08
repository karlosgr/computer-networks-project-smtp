import flet as ft
import src.services.mail_services as ems


def mail_page(page: ft.Page, options: ems.SmtpClientOption, function):
    """Mail Page"""

    email_service = ems.SmtpClientServices(options=options)

    mail_from: str = ""
    mail_to: str = ""
    subject: str = ""
    body: str = ""

    text = ft.Text(
        "",
        style=ft.TextStyle(
            color=ft.colors.GREEN,
            size=20,
        ),
    )

    def on_mail_from_change(control: ft.ControlEvent):
        nonlocal mail_from
        mail_from = str(control.control.value)

    def on_mail_to_change(control: ft.ControlEvent):
        nonlocal mail_to
        mail_to = str(control.control.value)

    def on_subject_change(control: ft.ControlEvent):
        nonlocal subject
        subject = str(control.control.value)

    def on_body_change(control: ft.ControlEvent):
        nonlocal body
        body = str(control.control.value)

    async def send_mail():
        error = await email_service.send_mail(
            receiver_mail=mail_to,
            sender_mail=mail_from,
            subject=subject,
            body=body,
        )
        if error is None:
            text.value = "Sended Email"

    page.add(
        ft.SafeArea(
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Container(
                        alignment=ft.alignment.center_left,
                        content=ft.IconButton(
                            icon=ft.icons.SETTINGS,
                            icon_color=ft.colors.BLACK,
                            icon_size=30,
                            on_click=function,
                        ),
                    ),
                    ft.Container(
                        height=20,
                    ),
                    ft.Text(
                        value="Mail Client",
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
                    ft.Row(
                        controls=[
                            ft.Container(
                                width=400,
                                content=ft.TextField(
                                    label="Sender Email",
                                    focused_color="blue",
                                    prefix_icon=ft.icons.SUBJECT_OUTLINED,
                                    cursor_color="black",
                                    color=ft.colors.BLACK26,
                                    on_change=on_mail_from_change,
                                ),
                            ),
                            ft.Container(
                                width=400,
                                content=ft.TextField(
                                    label="Receiver Email",
                                    focused_color="blue",
                                    prefix_icon=ft.icons.SUBJECT_OUTLINED,
                                    cursor_color="black",
                                    color=ft.colors.BLACK26,
                                    on_change=on_mail_to_change,
                                ),
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    ft.Container(
                        height=50,
                    ),
                    ft.Container(
                        width=400,
                        content=ft.TextField(
                            label="Subject",
                            focused_color="blue",
                            prefix_icon=ft.icons.SUBJECT_OUTLINED,
                            cursor_color="black",
                            color=ft.colors.BLACK26,
                            on_change=on_subject_change,
                        ),
                    ),
                    ft.Container(
                        height=20,
                    ),
                    ft.Container(
                        width=400,
                        content=ft.TextField(
                            label="Message",
                            focused_color="blue",
                            prefix_icon=ft.icons.MESSAGE_OUTLINED,
                            cursor_color="black",
                            color=ft.colors.BLACK26,
                            multiline=True,
                            min_lines=1,
                            max_lines=8,
                            on_change=on_body_change,
                        ),
                    ),
                    ft.Container(
                        height=20,
                    ),
                    ft.Container(
                        width=400,
                        content=ft.ElevatedButton(
                            text="Send", color="blue", height=50, on_click=send_mail
                        ),
                    ),
                    ft.Container(
                        height=20,
                    ),
                ],
            ),
        ),
    )
