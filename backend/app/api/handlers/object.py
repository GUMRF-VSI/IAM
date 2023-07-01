from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from api.deps import get_database

router = APIRouter()


@router.post("/", )
async def create_object(db: Session = Depends(get_database)):
    ...


@router.get("/{object_id}", )
async def get_object(db: Session = Depends(get_database)):
    ...


@router.put("/{object_id}", )
async def update_object(db: Session = Depends(get_database)):
    ...


@router.delete("/", )
async def create_object(db: Session = Depends(get_database)):
    ...


@router.get("/list", )
async def get_objects_list(db: Session = Depends(get_database)):
    ...
