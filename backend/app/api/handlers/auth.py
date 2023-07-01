from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from api.deps import get_database
from database import crud
from database.schemas import user as user_schemas
from config.security.token import get_token
from config.security.schemas import auth, token

router = APIRouter()


@router.post("/registration")
async def registration(user_data: user_schemas.UserCreate, db: Session = Depends(get_database)) -> token.TokenData:
    if crud.user.get_by_email(db=db, email=user_data.email):
        raise HTTPException(status_code=400, detail="Данный email уже используется")
    user = crud.user.create(db=db, obj_in=user_data)
    return get_token(user)


@router.post("/authorization")
async def authorization(auth_data: auth.UserAuth, db: Session = Depends(get_database)) -> token.TokenData:
    user = crud.user.authenticate(db=db, email=auth_data.email, password=auth_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Неверный email или пароль")
    return get_token(user)
