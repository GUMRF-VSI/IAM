from tortoise import fields

from models.base.base_model import CustomModel


class Action(CustomModel):
    name = fields.CharField(max_length=128)
    code = fields.CharField(max_length=128)

    class Meta:
        table = "action"
