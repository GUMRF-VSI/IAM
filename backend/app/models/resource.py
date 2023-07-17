from secrets import token_hex

from datetime import datetime

from tortoise import fields

from models.base.base_model import CustomModel


class Resource(CustomModel):
    name = fields.CharField(max_length=128)
    token = fields.CharField(max_length=32, default=token_hex(32))
    created_at = fields.DatetimeField(default=datetime.now())

    class Meta:
        table = 'resource'
