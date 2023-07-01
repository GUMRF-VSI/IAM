from fastapi import APIRouter, Depends, HTTPException, Query

from sqlalchemy.orm import Session

from database import crud
from api.deps import get_database
from database.schemas import user as user_schemas
from config.security.token import get_token

router = APIRouter()


@router.post("/", response_model=user_schemas.User)
def create_user(user_data: user_schemas.UserCreate, db: Session = Depends(get_database)):
    if crud.user.get_by_email(db=db, email=user_data.email):
        raise HTTPException(status_code=400, detail="Данный email уже используется")
    user = crud.user.create(db=db, obj_in=user_data)
    return get_token(user)


@router.get("/{user_id}", response_model=user_schemas.User)
async def get_user(user_id: int, db: Session = Depends(get_database)):
    user = crud.user.get(db=db, id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return user


@router.delete("/{user_id}")
async def delete_user(user_id: int, db: Session = Depends(get_database)):
    status = crud.user.remove(db=db, id=user_id)
    if not status:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return HTTPException(status_code=200)


@router.put("/{user_id}")
async def update_user(db: Session = Depends(get_database),
                      page: int = Query(ge=0, default=0),
                      size: int = Query(ge=1, le=100)) -> list:
    ...


@router.get("/list")
async def get_users_list(user_id: int, db: Session = Depends(get_database)):
    ...
