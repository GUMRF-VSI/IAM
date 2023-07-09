from models import Session
from security.utils.parse_token import parse_token
from schemas.token import RefreshToken, RefreshTokenData
from api import exceptions


async def validate_refresh_token(refresh_token: RefreshToken) -> RefreshTokenData:
    refresh_token_data = parse_token(refresh_token.refresh)

    session = await Session.filter(uuid=refresh_token_data.sid).first()

    if not session:
        raise exceptions.token.invalid_token

    return refresh_token_data
