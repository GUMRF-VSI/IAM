from sqlalchemy.orm import Session

from database.crud.base import CRUDBase
from database.models import models
from schemas import action as action_schemas


class CRUDAction(CRUDBase[models.Action, action_schemas.CreateAction, action_schemas.ActionUpdate]):
    def update(self, db: Session, *, db_obj: models.Action, obj_in: action_schemas.ActionUpdate) -> models.Action:
        obj_in.code = obj_in.code.value
        return super().update(db=db, db_obj=db_obj, obj_in=obj_in)


action = CRUDAction(models.Action)
