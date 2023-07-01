from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from api.deps import get_database

router = APIRouter()


@router.post("/", )
async def create_action(db: Session = Depends(get_database)):
    ...


@router.get("/{action_id}", )
async def get_action(db: Session = Depends(get_database)):
    ...


@router.put("/{action_id}", )
async def update_action(db: Session = Depends(get_database)):
    ...


@router.delete("/", )
async def create_action(db: Session = Depends(get_database)):
    ...


@router.get("/list", )
async def get_actions_list(db: Session = Depends(get_database)):
    ...
