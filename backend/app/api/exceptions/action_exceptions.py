from fastapi import HTTPException

from api.exceptions.base import BaseExceptions
from database.models.models import Action


class ActionExceptions(BaseExceptions):
    __404_message: str = 'не найдено'


action = ActionExceptions(Action)
