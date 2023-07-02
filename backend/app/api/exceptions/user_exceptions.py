from fastapi import HTTPException

from api.exceptions.base import BaseExceptions
from database.models.models import User


class UserExceptions(BaseExceptions):
    __invalid_cred_message: str = 'Неверный email или пароль'
    __duplicate_email_message: str = 'Данный email уже используется'

    @property
    def invalid_cred(self):
        return HTTPException(status_code=400, detail=self.__invalid_cred_message)

    @property
    def duplicate_email(self):
        raise HTTPException(status_code=400, detail=self.__duplicate_email_message)


user = UserExceptions(User)
