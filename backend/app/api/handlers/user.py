from uuid import UUID

from typing import List

from fastapi import APIRouter, Response, status

from api import exceptions
from models import user as user_models
from schemas import user as user_schemas
from db.shortcuts import get_object_or_404

router = APIRouter()


@router.post("/create", response_model=user_schemas.UserORM)
async def create_user(user_data: user_schemas.UserCreate) -> user_models.User:
    is_user_exist = await user_models.User.filter(email=user_data.email).exists()

    if is_user_exist:
        raise exceptions.user.duplicate_user

    db_user = user_models.User(**user_data.model_dump())
    db_user.set_password(user_data.password)
    await db_user.save()

    return db_user


@router.get('/list', response_model=List[user_schemas.UserORM])
async def users_list() -> List[user_models.User]:
    users = await user_models.User.all()
    return users


@router.get('/{user_id}', response_model=user_schemas.UserORM)
async def user_retrieve(user_id: UUID) -> user_models.User:
    db_user = await get_object_or_404(user_models.User, uuid=user_id)
    return db_user


@router.patch('/user_id', response_model=user_schemas.UserORM)
async def update_user(user_id: UUID, user_data: user_schemas.UserUpdate):
    db_user = await get_object_or_404(user_models.User, uuid=user_id)
    await db_user.update_from_dict(**user_data.model_dump())
    return db_user


@router.delete('/{user_id}')
async def delete_user(user_id: UUID):
    db_user = await get_object_or_404(user_models.User, uuid=user_id)
    await db_user.delete()
    return Response(status_code=status.HTTP_200_OK, content='success')
