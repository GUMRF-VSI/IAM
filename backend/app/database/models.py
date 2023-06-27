from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, Table, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from constants.types import ChoiceType
from constants.constants import OBJECTS, ACTIONS


Base = declarative_base()


role_permission = Table('roles_permissions', Base.metadata,
                        Column('role_id', ForeignKey('roles.id'), primary_key=True),
                        Column('permission_id', ForeignKey('permissions.id'), primary_key=True))

user_role = Table('user_role', Base.metadata,
                  Column('user_id', ForeignKey('users.id'), primary_key=True),
                  Column('role_id', ForeignKey('roles.id'), primary_key=True))


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, unique=True, index=True)

    email = Column(String, unique=True, index=True)
    last_name = Column(String, nullable=True)
    first_name = Column(String, nullable=True)
    middle_name = Column(String, nullable=True)

    is_active = Column(Boolean, default=True)
    last_login = Column(DateTime, nullable=True)

    created_at = Column(DateTime)
    updated_at = Column(DateTime, nullable=True)

    password = Column(String)

    roles = relationship("Role", secondary='user_role', back_populates='users')


class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, unique=True, index=True)
    name = Column(String)

    users = relationship("Role", secondary='user_role', back_populates='roles')
    permissions = relationship('Permission', secondary='role_permission', back_populates='roles')


class Permission(Base):
    __tablename__ = "permissions"

    id = Column(Integer, primary_key=True, unique=True, index=True)
    name = Column(String)

    object_id = Column(Integer, ForeignKey('objects.id'))
    action_id = Column(Integer, ForeignKey('actions.id'))

    roles = relationship('Role', secondary='role_permission', back_populates='permissions')


class Object(Base):
    __tablename__ = "objects"

    id = Column(Integer, primary_key=True, unique=True, index=True)
    name = Column(String)
    code = Column(ChoiceType(OBJECTS), nullable=False)


class Action(Base):
    __tablename__ = "actions"

    id = Column(Integer, primary_key=True, unique=True, index=True)
    name = Column(String)
    code = Column(ChoiceType(ACTIONS), nullable=False)
