from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from api.deps.databse import get_database

router = APIRouter()


@router.post("/", )  # TODO Доступ только для определенных ролей
async def create_role(db: Session = Depends(get_database)):
    ...  # TODO Логика создания ролей


@router.get("/{role_id}", )  # TODO Доступ только для определенных ролей
async def get_role(db: Session = Depends(get_database)):
    ...  # TODO Логика получения роли по id


@router.put("/{role_id}", )  # TODO Доступ только для определенных ролей
async def update_role(db: Session = Depends(get_database)):
    ...  # TODO Логика обновления роли


@router.delete("/", )  # TODO Доступ только для определенных ролей
async def delete_role(db: Session = Depends(get_database)):
    ...  # TODO Логика удаления роли по id


@router.get("/list", )  # TODO Доступ только для определенных ролей
async def get_roles_list(db: Session = Depends(get_database)):
    ...  # TODO Логика получения всех ролей
    ...  # TODO Логика фильтрации ролей
    ...  # TODO Логика пагинации
