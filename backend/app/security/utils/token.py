from jose import jwt

from config.settings import settings
from schemas import token as token_schemas
from api.exceptions import token as token_exceptions
from models import session as session_models


async def validate_access_token(token: str) -> token_schemas.AccessTokenData:
    token_data = parse_access_token(token)
    session = await session_models.Session.filter(uuid=token_data.sid).first()
    if not session:
        raise token_exceptions.invalid_token

    user = await session.user.exists()
    if not user:
        raise token_exceptions.invalid_token
    return token_data


def parse_access_token(token: str) -> token_schemas.AccessTokenData:
    parsed_token = parse_token(token)
    token_type = parsed_token.get('typ', None)

    if not token_type or token_type != 'Bearer':
        raise token_exceptions.unknown_token

    return token_schemas.AccessTokenData.parse_obj(parsed_token)


def parse_refresh_token(token: str) -> token_schemas.RefreshTokenData:
    parsed_token = parse_token(token)
    token_type = parsed_token.get('typ', None)

    if not token_type or token_type != 'Refresh':
        raise token_exceptions.unknown_token

    return token_schemas.RefreshTokenData.parse_obj(parsed_token)


def parse_identity_token(token: str) -> token_schemas.IdentityTokenData:
    parsed_token = parse_token(token)
    token_type = parsed_token.get('typ', None)

    if not token_type or token_type != 'Identity':
        raise token_exceptions.unknown_token

    return token_schemas.IdentityTokenData.parse_obj(parsed_token)


def parse_token(raw_token: str) -> dict:
    try:
        return jwt.decode(token=raw_token, key=settings.SECURITY.SECRET_KEY, options={'verify_exp': True, })
    except (jwt.JWTError, jwt.ExpiredSignatureError) as error:
        if error == 'Signature has expired.':
            raise token_exceptions.token_expired
        raise token_exceptions.invalid_token
