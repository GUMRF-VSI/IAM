from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from api.deps.databse import get_database
from database import crud
from schemas import user
from config.security import auth

router = APIRouter()


@router.post("/", response_model=user.UserORM)  # TODO Доступ только для определенных ролей
def create_user(user_data: user.UserCreate, db: Session = Depends(get_database)):
    if crud.user.get_by_email(db=db, email=user_data.email):
        raise HTTPException(status_code=400, detail="Данный email уже используется")
    db_user = crud.user.create(db=db, obj_in=user_data)
    return auth.token.generate_token(db_user)


@router.get("/{user_id}", response_model=user.UserORM)  # TODO Доступ только для определенных ролей
async def get_user(user_id: int, db: Session = Depends(get_database)):
    db_user = crud.user.get(db=db, id=user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return db_user


@router.delete("/{user_id}")  # TODO Доступ только для определенных ролей
async def delete_user(user_id: int, db: Session = Depends(get_database)):
    status = crud.user.remove(db=db, id=user_id)
    if not status:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return HTTPException(status_code=200)


@router.put("/{user_id}", response_model=user.UserORM)
async def update_user(user_id: int, user_data: user.UserUpdate,
                      db: Session = Depends(get_database)) -> user.UserORM:
    db_user = crud.user.get(db=db, id=user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return crud.user.update(db=db, db_obj=db_user, obj_in=user_data)


# @router.get("/list")  # TODO Доступ только для определенных ролей
async def get_users_list(db: Session = Depends(get_database)):
    ...  # TODO Логика получения всех пользователей
    ...  # TODO Логика фильтрации пользователей
    ...  # TODO Логика пагинации
