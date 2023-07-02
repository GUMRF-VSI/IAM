from fastapi import HTTPException

from api.exceptions.base import BaseExceptions
from database.models.models import Action


class ActionExceptions(BaseExceptions):
    __404_message: str = 'не найдено'

    @property
    def not_found(self):
        model_name = self.get_model_name()
        if model_name:
            return HTTPException(status_code=404, detail=f'{model_name} {self.__404_message}')
        else:
            return HTTPException(status_code=404, detail=f'{model_name} {self.__default_404_message}')


action = ActionExceptions(Action)
