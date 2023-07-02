from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from api.deps.databse import get_database

router = APIRouter()


@router.post("/", )  # TODO Доступ только для определенных ролей
async def create_permission(db: Session = Depends(get_database)):
    ...  # TODO Логика создания разрешений


@router.get("/{permission_id}", )  # TODO Доступ только для определенных ролей
async def get_permission(db: Session = Depends(get_database)):
    ...  # TODO Логика получения разрешения по id


@router.put("/{permission_id}", )  # TODO Доступ только для определенных ролей
async def update_permission(db: Session = Depends(get_database)):
    ...  # TODO Логика обновления разрешения


@router.delete("/", )  # TODO Доступ только для определенных ролей
async def delete_permission(db: Session = Depends(get_database)):
    ...  # TODO Логика удаления разрешения по id


@router.get("/list", )  # TODO Доступ только для определенных ролей
async def get_permissions_list(db: Session = Depends(get_database)):
    ...  # TODO Логика получения всех разрешений
    ...  # TODO Логика фильтрации разрешений
    ...  # TODO Логика пагинации
