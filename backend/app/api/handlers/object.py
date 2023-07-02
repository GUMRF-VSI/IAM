from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from database import crud
from schemas import object
from api.deps.databse import get_database

router = APIRouter()


@router.post("/", response_model=object.ObjectORM)  # TODO Доступ только для определенных ролей
async def create_object(object_data: object.CreateObject, db: Session = Depends(get_database)) -> object.ObjectORM:
    return crud.obj.create(db=db, obj_in=object_data)


@router.get("/{object_id}", response_model=object.ObjectORM)  # TODO Доступ только для определенных ролей
async def get_object(action_id: int, db: Session = Depends(get_database)) -> object.ObjectORM:
    db_object = crud.obj.get(db=db, id=action_id)
    if not db_object:
        raise HTTPException(status_code=404, detail="Объект не найдено")
    return db_object


@router.put("/{object_id}", response_model=object.ObjectORM)  # TODO Доступ только для определенных ролей
async def update_object(object_id: int, object_data: object.ObjectUpdate,
                        db: Session = Depends(get_database)) -> object.ObjectORM:
    db_action = crud.obj.get(db=db, id=object_id)
    if not db_action:
        raise HTTPException(status_code=404, detail="Объект не найдено")
    return crud.obj.update(db=db, db_obj=db_action, obj_in=object_data)


@router.delete("/{object_id}")  # TODO Доступ только для определенных ролей
async def delete_object(object_id: int, db: Session = Depends(get_database)):
    status = crud.obj.remove(db=db, id=object_id)
    if not status:
        raise HTTPException(status_code=404, detail="Объект не найдено")
    return HTTPException(status_code=200)


# @router.get("/list", )  # TODO Доступ только для определенных ролей
async def get_objects_list(db: Session = Depends(get_database)):
    ...  # TODO Логика получения всех объектов
    ...  # TODO Логика фильтрации объектов
    ...  # TODO Логика пагинации
