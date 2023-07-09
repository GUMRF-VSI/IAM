from tortoise import fields

from models.base.base_model import CustomModel


class Role(CustomModel):
    name = fields.CharField(max_length=128)

    permissions = fields.ManyToManyField('models.Permission', related_name='permissions',
                                         through='role_permission')

    class Meta:
        table = "role"
