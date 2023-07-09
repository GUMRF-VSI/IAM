import base64


def base64url_encode(data: str):
    b_string = bytes(data, 'utf-8')
    return base64.urlsafe_b64encode(b_string)
