import flet as ft
import src.services.mail_services as ems
import src.services.file_services as fs


def mail_page(page: ft.Page, options: ems.SmtpClientOption, function):
    """Mail Page"""

    print(options.smtp_server)
    email_service = ems.SmtpClientServices(options=options)

    mail_from: str = ""
    mail_to: str = ""
    subject: str = ""
    body: str = ""

    selected_file: ft.FilePickerFileType

    is_file_selected: bool = False

    def pick_file_result(e: ft.FilePickerResultEvent):
        nonlocal selected_file
        selected_file = e.files[0]
        nonlocal is_file_selected
        is_file_selected = True

    file_picker = ft.FilePicker(on_result=pick_file_result)

    page.overlay.append(file_picker)

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

    def pick_file(_):
        print("picking file")
        file_picker.pick_files(allow_multiple=True)

    def send_mail(_):
        error = email_service.send_mail(
            receiver_mail=mail_to,
            sender_mail=mail_from,
            subject=subject,
            body=body,
            attachments_files=(
                fs.encode_file(file_path=selected_file) if is_file_selected else ""
            ),
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
                        content=ft.IconButton(
                            height=50,
                            on_click=pick_file,
                            icon=ft.icons.UPLOAD_FILE,
                            content=ft.Text("Select File"),
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
