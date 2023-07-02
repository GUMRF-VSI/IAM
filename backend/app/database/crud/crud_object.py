from sqlalchemy.orm import Session

from database.crud.base import CRUDBase
from database.models import models
from schemas import object as object_schemas


class CRUDObject(CRUDBase[models.Object, object_schemas.CreateObject, object_schemas.ObjectUpdate]):
    def update(self, db: Session, *, db_obj: models.Object, obj_in: object_schemas.ObjectUpdate) -> models.Object:
        obj_in.code = obj_in.code.value
        return super().update(db=db, db_obj=db_obj, obj_in=obj_in)


obj = CRUDObject(models.Object)
