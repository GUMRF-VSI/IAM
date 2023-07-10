from jose import jwt

from datetime import datetime, timedelta

from config.settings import settings
from schemas import token
from models.user import User
from models.session import Session
from models.utils.user import get_user_riles


async def create_access_token(user: User, session: Session, exp: int, iat: int, auth_time: int) -> str:
    roles = await get_user_riles(user)
    access_token_data = token.AccessTokenData(exp=exp, sid=session.uuid.__str__(), iat=iat,
                                              sub=user.uuid.__str__(), auth_time=auth_time, roles=roles)
    return jwt.encode(access_token_data.dict(), settings.SECURITY.SECRET_KEY, settings.SECURITY.ALGORITHM)


def __create_refresh_token(user: User, session: Session, exp: int, iat: int) -> str:
    refresh_token_data = token.RefreshTokenData(exp=exp, sid=session.uuid.__str__(), iat=iat,
                                                sub=user.uuid.__str__())
    return jwt.encode(refresh_token_data.dict(), settings.SECURITY.SECRET_KEY, settings.SECURITY.ALGORITHM)


def __create_identity_token(user: User, session: Session, exp: int, iat: int) -> str:
    identity_token_data = token.IdentityTokenData(
        exp=exp, iat=iat, sid=session.uuid.__str__(), sub=user.uuid.__str__(), email=user.email,
        last_name=user.last_name,
        first_name=user.first_name, middle_name=user.middle_name, is_active=user.is_active
    )
    return jwt.encode(identity_token_data.dict(), settings.SECURITY.SECRET_KEY, settings.SECURITY.ALGORITHM)


async def generate_tokens(user: User, session: Session,
                          expires_delta: int = settings.SECURITY.ACCESS_TOKEN_EXPIRE_MINUTES) -> token.Tokens:
    datetime_now = datetime.utcnow()

    exp = int((datetime_now + timedelta(expires_delta)).timestamp())
    iat = int(datetime_now.timestamp())

    access_token = await create_access_token(user=user, session=session, exp=exp, iat=iat,
                                             auth_time=int(datetime_now.timestamp()))

    return token.Tokens(
        access=access_token,
        refresh=__create_refresh_token(user=user, session=session, exp=exp, iat=iat),
        identity=__create_identity_token(user=user, session=session, exp=exp, iat=iat)
    )
