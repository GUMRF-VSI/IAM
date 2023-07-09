from tortoise import Model, fields


class CustomModel(Model):
    id = fields.IntField(pk=True, unique=True, index=True)

    class Meta:
        abstract = True
