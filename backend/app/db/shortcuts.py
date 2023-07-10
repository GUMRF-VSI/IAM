from typing import TypeVar, Type

from api.exceptions.base import BaseExceptions
from models.base.base_model import CustomModel


ModelType = TypeVar("ModelType", bound=CustomModel)


async def get_object_or_404(model: Type[ModelType], **filters):
    exception = BaseExceptions(model)
    db_object = await model.filter(**filters).first()
    if not db_object:
        raise exception.not_found
    return db_object
