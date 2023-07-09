from uuid import UUID

from fastapi import APIRouter, Response, status

import models
from schemas import user, token
from api import exceptions
from models.utils.session import get_or_create_session
from security.token.generation import generate_tokens

router = APIRouter()


@router.post("/create")
async def create_user(user_data: user.UserCreate) -> token.Tokens:
    is_user_exist = await models.User.filter(email=user_data.email).exists()

    if is_user_exist:
        raise exceptions.user.duplicate_user

    db_user = models.User(**user_data.model_dump())
    db_user.set_password(user_data.password)
    await db_user.save()

    session = await get_or_create_session(db_user)

    tokens = await generate_tokens(user=db_user, session=session)

    return tokens
