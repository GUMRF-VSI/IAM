from uuid import UUID

from typing import List

from fastapi import APIRouter, status, Depends
from fastapi.responses import JSONResponse

from tortoise.exceptions import OperationalError

from api import exceptions, deps
from models import user as user_models
from schemas import user as user_schemas
from db.shortcuts import get_object_or_404
from security.permission import user as user_permissions

router = APIRouter()


@router.post("/create", response_model=user_schemas.UserORM,
             dependencies=[Depends(user_permissions.check_create_permission)])
async def create_user(user_data: user_schemas.UserCreate) -> user_models.User:
    is_user_exist = await user_models.User.filter(email=user_data.email).exists()

    if is_user_exist:
        raise exceptions.user.duplicate_user

    db_user = user_models.User(**user_data.dict())
    db_user.set_password(user_data.password)
    await db_user.save()

    return db_user


@router.get('/list', response_model=List[user_schemas.UserORM],
            dependencies=[Depends(user_permissions.check_retrieve_permission)])
async def users_list() -> List[user_models.User]:
    users = await user_models.User.all()
    return users


@router.get('/{user_id}', response_model=user_schemas.UserORM,
            dependencies=[Depends(user_permissions.check_retrieve_permission)])
async def user_retrieve(user_id: UUID) -> user_models.User:
    db_user = await get_object_or_404(user_models.User, uuid=user_id)
    return db_user


@router.patch('/{user_id}', response_model=user_schemas.UserORM,
              dependencies=[Depends(user_permissions.check_update_permission)])
async def update_user(user_id: UUID, user_data: user_schemas.UserUpdate):
    db_user = await get_object_or_404(user_models.User, uuid=user_id)
    await db_user.update_from_dict(**user_data.dict())
    return db_user


@router.delete('/{user_id}', dependencies=[Depends(user_permissions.check_delete_permission)])
async def delete_user(user_id: UUID):
    db_user = await get_object_or_404(user_models.User, uuid=user_id)
    await db_user.delete()
    return Response(status_code=status.HTTP_200_OK, content='success')


@router.post('/reset-password')
async def reset_password(data: user_schemas.ResetPassword,
                         user: user_models.User = Depends(deps.token.validate_access_token)) -> JSONResponse:
    if not user.check_password(data.old_password):
        raise exceptions.user.not_correct_odl_password

    user.set_password(data.new_password)
    try:
        await user.save()
    except OperationalError:
        JSONResponse(status_code=status.HTTP_200_OK, content={'success': False})
    return JSONResponse(status_code=status.HTTP_200_OK, content={'success': True})
