import uuid

from datetime import datetime

from tortoise import fields

from models.base.base_model import CustomModel


class Session(CustomModel):
    uuid = fields.UUIDField(index=True, unique=True, default=uuid.uuid4())
    user = fields.ForeignKeyField('models.User', related_name='sessions')
    created_at = fields.DatetimeField(default=datetime.now())

    class Meta:
        table = 'session'
