import base64


def encode_file(file_path: str) -> str:
    """Encode a file in base64"""
    file = open(file_path, "rb")
    file_encoded = base64.b64encode(file.read()).decode()
    encoded_str = ""
    encoded_str += f"Content-Type: {file.mode}; name={file.name}\r\n"
    encoded_str += f"Content-Disposition: attachment; filename={file.name}\r\n"
    encoded_str += "Content-Transfer-Encoding: base64\r\n"
    encoded_str += f"\r\n{file_encoded}\r\n.\r\n"
