from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from api.deps.databse import get_database

router = APIRouter()


@router.post("/", )  # TODO Доступ только для определенных ролей
async def create_action(db: Session = Depends(get_database)):
    ...  # TODO Логика создания действий


@router.get("/{action_id}", )  # TODO Доступ только для определенных ролей
async def get_action(db: Session = Depends(get_database)):
    ...  # TODO Логика получения действия по id


@router.put("/{action_id}", )  # TODO Доступ только для определенных ролей
async def update_action(db: Session = Depends(get_database)):
    ...  # TODO Логика обновления действия


@router.delete("/", )  # TODO Доступ только для определенных ролей
async def delete_action(db: Session = Depends(get_database)):
    ...  # TODO Логика удаления действия по id


@router.get("/list", )  # TODO Доступ только для определенных ролей
async def get_actions_list(db: Session = Depends(get_database)):
    ...  # TODO Логика получения всех действий
    ...  # TODO Логика фильтрации действий
    ...  # TODO Логика пагинации
