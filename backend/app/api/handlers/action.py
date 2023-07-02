from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from database import crud
from schemas import action
from api.deps.databse import get_database
from api import exceptions

router = APIRouter()


@router.post("/", response_model=action.ActionORM)  # TODO Доступ только для определенных ролей
async def create_action(action_data: action.CreateAction, db: Session = Depends(get_database)) -> action.ActionORM:
    return crud.action.create(db=db, obj_in=action_data)


@router.get("/{action_id}", response_model=action.ActionORM)  # TODO Доступ только для определенных ролей
async def get_action(action_id: int, db: Session = Depends(get_database)) -> action.ActionORM:
    db_action = crud.action.get(db=db, id=action_id)
    if not db_action:
        raise exceptions.action.not_found
    return db_action


@router.put("/{action_id}", response_model=action.ActionORM)  # TODO Доступ только для определенных ролей
async def update_action(action_id: int, action_data: action.ActionUpdate,
                        db: Session = Depends(get_database)) -> action.ActionORM:
    db_action = crud.action.get(db=db, id=action_id)
    if not db_action:
        raise exceptions.action.not_found
    return crud.action.update(db=db, db_obj=db_action, obj_in=action_data)


@router.delete("/{action_id}", )  # TODO Доступ только для определенных ролей
async def delete_action(action_id: int, db: Session = Depends(get_database)):
    status = crud.action.remove(db=db, id=action_id)
    if not status:
        raise exceptions.action.not_found
    return HTTPException(status_code=200)


# @router.get("/list", )  # TODO Доступ только для определенных ролей
async def get_actions_list(db: Session = Depends(get_database)):
    ...  # TODO Логика получения всех действий
    ...  # TODO Логика фильтрации действий
    ...  # TODO Логика пагинации
