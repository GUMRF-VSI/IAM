from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from api.deps.databse import get_database

router = APIRouter()


@router.post("/", )  # TODO Доступ только для определенных ролей
async def create_object(db: Session = Depends(get_database)):
    ...  # TODO Логика создания объектов


@router.get("/{object_id}", )  # TODO Доступ только для определенных ролей
async def get_object(db: Session = Depends(get_database)):
    ...  # TODO Логика получения объекта по id


@router.put("/{object_id}", )  # TODO Доступ только для определенных ролей
async def update_object(db: Session = Depends(get_database)):
    ...  # TODO Логика обновления объекта


@router.delete("/", )  # TODO Доступ только для определенных ролей
async def delete_object(db: Session = Depends(get_database)):
    ...  # TODO Логика удаления объекта по id


@router.get("/list", )  # TODO Доступ только для определенных ролей
async def get_objects_list(db: Session = Depends(get_database)):
    ...  # TODO Логика получения всех объектов
    ...  # TODO Логика фильтрации объектов
    ...  # TODO Логика пагинации
