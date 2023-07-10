from typing import TypeVar, Type

from models.base.base_model import CustomModel
from config.constants import ActionsTypes
from models import user as user_models
from api.exceptions import user as user_exceptions
from security.utils.token import validate_access_token


ModelType = TypeVar("ModelType", bound=CustomModel)


async def check_permissions(token: str, model: Type[ModelType], action: ActionsTypes) -> user_models.User:
    token_data = await validate_access_token(token)
    for role in token_data.roles:
        for obj, actions in role.items():
            if obj == model.Meta.table and action.name in actions:
                return await user_models.User.filter(uuid=token_data.sub).first()
    raise user_exceptions.forbidden
