from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session

from config.security import password
from database.crud.base import CRUDBase
from database.models import models
from schemas import user as user_schemas


class CRUDUser(CRUDBase[models.User, user_schemas.UserCreate, user_schemas.UserUpdate]):
    def get_by_email(self, db: Session, *, email: str) -> Optional[models.User]:
        return db.query(self.model).filter(self.model.email == email).first()

    def create(self, db: Session, *, obj_in: user_schemas.UserCreate) -> models.User:
        db_obj = self.model(email=obj_in.email,
                            last_name=obj_in.last_name,
                            first_name=obj_in.first_name,
                            middle_name=obj_in.middle_name,
                            password=password.get_password_hash(obj_in.password))
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
            self, db: Session, *, db_obj: models.User, obj_in: Union[user_schemas.UserUpdate, Dict[str, Any]]
    ) -> models.User:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        if update_data["password"]:
            update_data["password"] = password.get_password_hash(update_data["password"])
        return super().update(db, db_obj=db_obj, obj_in=update_data)

    def remove(self, db: Session, *, id: int) -> bool:
        db_user = self.get(db=db, id=id)
        if not db_user:
            return False
        db.delete(db_user)
        db.commit()
        return True

    def authenticate(self, db: Session, *, email: str, raw_password: str) -> Optional[models.User]:
        db_user = self.get_by_email(db, email=email)
        if not db_user:
            return None
        if not password.verify_password(raw_password, db_user.password):
            return None
        db_user.set_last_login()
        db.add(db_user)
        db.commit()
        return db_user

    def is_active(self, db_obj: models.User) -> bool:
        return db_obj.is_active

    def is_superuser(self, db_obj: models.User) -> bool:
        return db_obj.is_superuser


user = CRUDUser(models.User)
