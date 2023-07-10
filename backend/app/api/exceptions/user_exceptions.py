from fastapi import HTTPException, status

from api.exceptions.base import BaseExceptions
from models.user import User


class UserExceptions(BaseExceptions):
    __duplicate_user_message: str = 'User with this Email already exist!'
    __unknown_id: str = 'Unknown ID'
    __not_correct_old_password = 'Old password not correct'
    __forbidden = 'You do not have enough permission'

    @property
    def duplicate_user(self):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=self.__duplicate_user_message)

    @property
    def unknown_id(self):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=self.__unknown_id)

    @property
    def not_correct_odl_password(self):
        return HTTPException(status.HTTP_400_BAD_REQUEST, detail=self.__not_correct_old_password)

    @property
    def forbidden(self):
        return HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=self.__forbidden)


user = UserExceptions(User)
