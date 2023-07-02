from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from database import crud
from config.security import schemas, token
from schemas import user as user_schemas
from api.deps.databse import get_database
from api import exceptions

router = APIRouter()


@router.post("/registration")
async def registration(user_data: user_schemas.UserCreate,
                       db: Session = Depends(get_database)) -> schemas.TokenData:
    if crud.user.get_by_email(db=db, email=user_data.email):
        raise exceptions.user.duplicate_email
    user = crud.user.create(db=db, obj_in=user_data)
    return token.generate_token(user)


@router.post("/authorization")
async def authorization(auth_data: schemas.UserAuth,
                        db: Session = Depends(get_database)) -> schemas.TokenData:
    user = crud.user.authenticate(db=db, email=auth_data.email, raw_password=auth_data.password)
    if not user:
        raise exceptions.user.invalid_cred
    return token.generate_token(user)
