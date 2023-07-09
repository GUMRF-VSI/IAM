from fastapi import Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials


class TokenDeps:
    token_key = HTTPBearer()

    @staticmethod
    def validate_access_token(access_token: HTTPAuthorizationCredentials = Security(token_key)):
        ...

    @staticmethod
    def identity_access_token(identity_token: HTTPAuthorizationCredentials = Security(token_key)):
        ...


token = TokenDeps()
