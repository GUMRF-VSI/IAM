from jose import jwt

from typing import Union

from config.settings import settings
from schemas import token
from api import exceptions


def parse_token(raw_token: str) -> Union[token.AccessTokenData, token.RefreshTokenData, token.IdentityTokenData]:
    parsed_token = jwt.decode(token=raw_token, key=settings.SECURITY.SECRET_KEY, options={'verify_exp': True})
    token_type = parsed_token.get('typ', None)

    if not token_type:
        raise exceptions.token.unknown_token

    match token_type:
        case 'Bearer':
            return token.AccessTokenData.model_validate(parsed_token)
        case 'Refresh':
            return token.RefreshTokenData.model_validate(parsed_token)
        case 'Identity':
            return token.IdentityTokenData.model_validate(parsed_token)

    raise exceptions.token.unknown_token
