from fastapi import HTTPException, status

from api.exceptions.base import BaseExceptions
from models.user import User


class AuthExceptions(BaseExceptions):
    __invalid_cred_message: str = 'Incorrect Email or Password'
    __duplicate_user_message: str = 'User with this Email already exist!'
    __unknown_id: str = 'Unknown ID'

    @property
    def invalid_cred(self):
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=self.__invalid_cred_message)


auth = AuthExceptions(User)
