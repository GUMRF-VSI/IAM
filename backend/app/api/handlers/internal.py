from fastapi import APIRouter, status, Depends
from fastapi.responses import JSONResponse

from api import exceptions
from models import user as user_models
from schemas import internal as internal_schemas, user as user_schemas
from security.utils import token as token_utils
from security.token.validation import validate_resource_token

router = APIRouter()


@router.post('/token/verify', dependencies=[Depends(validate_resource_token)])
async def verify_access_token(data: internal_schemas.AccessToken) -> JSONResponse:
    token_data = await token_utils.validate_access_token(data.access_token)
    user = await user_models.User.filter(uuid=token_data.sub).first()
    if not user:
        return JSONResponse(status_code=status.HTTP_200_OK, content={'is_valid': False})
    return JSONResponse(status_code=status.HTTP_200_OK, content={'is_valid': True})


@router.get('/user', response_model=user_schemas.UserORM, dependencies=[Depends(validate_resource_token)])
async def get_user(data: internal_schemas.AccessToken) -> user_models.User:
    token_data = await token_utils.validate_access_token(data.access_token)
    user = await user_models.User.filter(uuid=token_data.sub).first()
    if not user:
        raise exceptions.user.not_found
    return user
