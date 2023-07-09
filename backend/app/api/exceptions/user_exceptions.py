from fastapi import HTTPException, status

from api.exceptions.base import BaseExceptions
from models.user import User


class UserExceptions(BaseExceptions):
    __invalid_cred_message: str = 'Неверный email или пароль'
    __duplicate_user_message: str = 'User with this Email already exist!'
    __unknown_id: str = 'Unknown ID'

    @property
    def invalid_cred(self):
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=self.__invalid_cred_message)

    @property
    def duplicate_user(self):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=self.__duplicate_user_message)

    @property
    def unknown_id(self):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=self.__unknown_id)


user = UserExceptions(User)
