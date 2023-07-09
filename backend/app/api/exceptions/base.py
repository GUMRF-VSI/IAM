from typing import TypeVar, Type, Optional

from fastapi import HTTPException, status

from models.base.base_model import CustomModel

ModelType = TypeVar("ModelType", bound=CustomModel)


class BaseExceptions:
    model: ModelType
    __404_message: str = 'не найден'
    __default_404_message: str = 'Не найдено'

    def __init__(self, model: Type[ModelType]):
        self.model = model

    def get_model_name(self) -> Optional[str]:
        return self.model.Meta.table.capitalize()

    @property
    def not_found(self):
        model_name = self.get_model_name()
        if model_name:
            return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'{model_name} {self.__404_message}')
        else:
            return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=self.__default_404_message)
