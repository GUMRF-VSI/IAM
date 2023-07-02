from typing import TypeVar, Type, Optional

from fastapi import HTTPException

from database.core.base_class import BaseModel
from constants.objects import OBJECTS

ModelType = TypeVar("ModelType", bound=BaseModel)


class BaseExceptions:
    model: ModelType
    __404_message: str = 'не найден'
    __default_404_message: str = 'Не найдено'

    def __init__(self, model: Type[ModelType]):
        self.model = model

    def get_model_name(self) -> Optional[str]:
        return OBJECTS.get(self.model.__tablename__)

    @property
    def not_found(self):
        model_name = self.get_model_name()
        if model_name:
            return HTTPException(status_code=404, detail=f'{model_name} {self.__404_message}')
        else:
            return HTTPException(status_code=404, detail=self.__default_404_message)
