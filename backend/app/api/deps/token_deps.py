from fastapi import Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from models import user as user_models


class TokenDeps:
    token_key = HTTPBearer()

    @staticmethod
    async def validate_access_token(access_token: HTTPAuthorizationCredentials = Security(token_key)) -> user_models.User:
        return await user_models.User.first()

    @staticmethod
    def identity_access_token(identity_token: HTTPAuthorizationCredentials = Security(token_key)):
        ...


token = TokenDeps()
