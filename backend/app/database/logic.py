from sqlalchemy.orm import Session

from database.models import models
from database.schemas import create as create_schemas


def create_user(db: Session, user: create_schemas.UserCreateSchema):
    ...


def create_role(db: Session, role: create_schemas.RoleCreateSchema):
    ...


def create_permission(db: Session, permission: create_schemas.PermissionCreateSchema):
    ...


def create_action(db: Session, action: create_schemas.ActionsCreateSchema):
    ...


def create_object(db: Session, _object: create_schemas.ObjectCreateSchema):
    ...
