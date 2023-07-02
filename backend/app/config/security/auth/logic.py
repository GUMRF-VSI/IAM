from jose import jwt

from datetime import datetime, timedelta

from config.settings import settings
from database.models import models
from config.security.schemas import token as token_schemas
from config.security.core.base import fernet


class TokenLogic:
    def generate_token(self, user: models.User) -> token_schemas.TokenData:
        return token_schemas.TokenData(access=self.create_access_token(user=user),
                                       refresh=self.create_refresh_token(user=user),
                                       identity=self.create_identity_token(user=user))

    @staticmethod
    def create_access_token(user: models.User,
                            expires_delta: int = settings.SECURITY.ACCESS_TOKEN_EXPIRE_MINUTES) -> str:
        expire_datetime = datetime.utcnow() + timedelta(expires_delta)
        expire_timestamp = int(expire_datetime.timestamp())

        access_token = token_schemas.AccessTokenData(exp=expire_timestamp, sub=user.get_sub())

        return jwt.encode(access_token.dict(), settings.SECURITY.SECRET_KEY, settings.SECURITY.ALGORITHM)

    @staticmethod
    def create_refresh_token(user: models.User):
        refresh_token = token_schemas.RefreshData(id=user.id, email=user.email)
        return fernet.encrypt(bytes(refresh_token.json().encode('utf-8')))

    @staticmethod
    def create_identity_token(user: models.User):
        data = dict(email=user.email)

        if user.last_name:
            data.update(last_name=user.last_name)
        if user.first_name:
            data.update(first_name=user.first_name)
        if user.middle_name:
            data.update(middle_name=user.middle_name)

        identity_token = token_schemas.RefreshData(id=user.id, email=user.email)

        return fernet.encrypt(bytes(identity_token.json().encode('utf-8')))


token = TokenLogic()
