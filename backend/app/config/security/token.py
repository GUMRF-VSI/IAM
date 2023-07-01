from jose import jwt

from datetime import datetime, timedelta

from config.settings import settings
from database.models.models import User
from config.security.schemas import token
from config.security.core.base import fernet


def get_token(user: User) -> token.TokenData:
    return token.TokenData(access=create_access_token(user=user),
                           refresh=create_refresh_token(user=user),
                           identity=create_identity_token(user=user))


def create_access_token(user: User, expires_delta: int = settings.SECURITY.ACCESS_TOKEN_EXPIRE_MINUTES) -> str:
    expire_datetime = datetime.utcnow() + timedelta(expires_delta)
    expire_timestamp = int(expire_datetime.timestamp())

    access_token = token.AccessTokenData(exp=expire_timestamp, sub=user.get_sub())

    return jwt.encode(access_token.dict(), settings.SECURITY.SECRET_KEY, settings.SECURITY.ALGORITHM)


def create_refresh_token(user: User):
    refresh_token = token.RefreshData(id=user.id, email=user.email)
    return fernet.encrypt(bytes(refresh_token.json().encode('utf-8')))


def create_identity_token(user: User):
    data = dict(email=user.email)

    if user.last_name:
        data.update(last_name=user.last_name)
    if user.first_name:
        data.update(first_name=user.first_name)
    if user.middle_name:
        data.update(middle_name=user.middle_name)

    identity_token = token.RefreshData(id=user.id, email=user.email)

    return fernet.encrypt(bytes(identity_token.json().encode('utf-8')))
