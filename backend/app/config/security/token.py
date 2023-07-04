from datetime import datetime, timedelta

from jose import jwt

from config.settings import settings
from config.security import schemas
from database.models import models


def generate_token(user: models.User,
                   expires_delta: int = settings.SECURITY.ACCESS_TOKEN_EXPIRE_MINUTES) -> schemas.TokenData:
    datetime_now = datetime.utcnow()

    exp = int((datetime_now + timedelta(expires_delta)).timestamp())
    iat = int(datetime_now.timestamp())

    return schemas.TokenData(
        access=create_access_token(user=user, exp=exp, iat=iat, auth_time=int(datetime_now.timestamp())),
        refresh=create_refresh_token(user=user, exp=exp, iat=iat),
        identity=create_identity_token(user=user, exp=exp, iat=iat)
    )


def create_access_token(user: models.User, exp: int, iat: int, auth_time: int) -> str:
    access_token_data = schemas.AccessTokenData(exp=exp, iat=iat, sub=user.id, auth_time=auth_time)
    return jwt.encode(access_token_data.dict(), settings.SECURITY.SECRET_KEY, settings.SECURITY.ALGORITHM)


def create_refresh_token(user: models.User, exp: int, iat: int) -> str:
    refresh_token_data = schemas.RefreshData(exp=exp, iat=iat, sub=user.id, sid=user.get_sid())
    return jwt.encode(refresh_token_data.dict(), settings.SECURITY.SECRET_KEY, settings.SECURITY.ALGORITHM)


def create_identity_token(user: models.User, exp: int, iat: int) -> str:
    identity_token_data = schemas.IdentityData(
        exp=exp, iat=iat, sub=user.id, email=user.email, last_name=user.last_name,
        first_name=user.first_name, middle_name=user.middle_name, is_active=user.is_active
    )
    return jwt.encode(identity_token_data.dict(), settings.SECURITY.SECRET_KEY, settings.SECURITY.ALGORITHM)
