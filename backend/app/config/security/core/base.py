import base64

from passlib.context import CryptContext

from config.settings import settings


def base64url_encode(data: str):
    b_string = bytes(data, 'utf-8')
    print(b_string)
    return base64.urlsafe_b64encode(b_string)


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
