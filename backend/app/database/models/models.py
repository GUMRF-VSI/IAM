import datetime

from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, Table, DateTime
from sqlalchemy.orm import relationship

from database.models.types import ChoiceType
from database.core.base_class import Base
from config.constants import OBJECTS, ACTIONS

role_permission = Table('role_permission', Base.metadata,
                        Column('role_id', ForeignKey('role.id'), primary_key=True),
                        Column('permission_id', ForeignKey('permission.id'), primary_key=True))

user_role = Table('user_role', Base.metadata,
                  Column('user_id', ForeignKey('user.id'), primary_key=True),
                  Column('role_id', ForeignKey('role.id'), primary_key=True))


class User(Base):
    id = Column(Integer, primary_key=True, unique=True, index=True)

    email: str = Column(String, unique=True, index=True)
    last_name = Column(String, nullable=True)
    first_name = Column(String, nullable=True)
    middle_name = Column(String, nullable=True)

    is_active = Column(Boolean, default=True)
    last_login = Column(DateTime, nullable=True)

    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, nullable=True)

    password = Column(String)

    roles = relationship("Role", secondary=user_role, back_populates='users')

    def set_last_login(self):
        self.last_login = datetime.datetime.utcnow()

    def get_sub(self):
        """Преобразуем строку в 2-ый формат, а затем в 16-ое число"""
        return hex(int(''.join(format(x, 'b') for x in bytearray(self.email, 'utf-8')), 2))

    def check_sub(self, sub: str):
        return sub == self.get_sub()


class Role(Base):
    id = Column(Integer, primary_key=True, unique=True, index=True)
    name = Column(String)

    users = relationship("User", secondary=user_role, back_populates='roles')
    permissions = relationship('Permission', secondary=role_permission, back_populates='roles')


class Permission(Base):
    id = Column(Integer, primary_key=True, unique=True, index=True)
    name = Column(String)

    object_id = Column(Integer, ForeignKey('object.id'))
    action_id = Column(Integer, ForeignKey('action.id'))

    roles = relationship('Role', secondary=role_permission, back_populates='permissions')


class Object(Base):
    id = Column(Integer, primary_key=True, unique=True, index=True)
    name = Column(String)
    code = Column(ChoiceType(OBJECTS), nullable=False)


class Action(Base):
    id = Column(Integer, primary_key=True, unique=True, index=True)
    name = Column(String)
    code = Column(ChoiceType(ACTIONS), nullable=False)
