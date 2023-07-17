from fastapi import Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from api import exceptions
from schemas.token import RefreshToken
from security.utils import token as token_utils
from models import session as session_models, user as user_models, resource as resource_models

token_key = HTTPBearer()


async def validate_resource_token(
        auth_token: HTTPAuthorizationCredentials = Security(token_key)) -> resource_models.Resource:
    resource = await resource_models.Resource.filter(token=auth_token.credentials).first()
    if not resource:
        raise exceptions.token.invalid_token
    return resource


async def validate_access_token(auth_token: HTTPAuthorizationCredentials = Security(token_key)) -> user_models.User:
    token_data = await token_utils.validate_access_token(auth_token.credentials)
    return await user_models.User.filter(uuid=token_data.sub).first()


async def validate_refresh_token(refresh_token: RefreshToken) -> session_models.Session:
    refresh_token_data = token_utils.parse_refresh_token(refresh_token.refresh)

    session = await session_models.Session.filter(uuid=refresh_token_data.sid).first()

    if not session:
        raise exceptions.token.invalid_token

    return session
