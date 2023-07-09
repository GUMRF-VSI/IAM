from tortoise import fields

from models.base.base_model import CustomModel


class Permission(CustomModel):
    name = fields.CharField(max_length=128)

    object = fields.ForeignKeyField('models.Object', related_name='permissions')
    action = fields.ForeignKeyField('models.Action', related_name='permissions')

    class Meta:
        table = "permission"
