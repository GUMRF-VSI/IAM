import uuid

from tortoise import fields

from models.base.base_user import AbstractUser

from models.validators import password, email


class User(AbstractUser):
    uuid = fields.UUIDField(index=True, unique=True, default=uuid.uuid4())
    email = fields.CharField(max_length=128, unique=True, index=True,
                             validators=[email.EmailValidator()])

    last_name = fields.CharField(max_length=128, null=True)
    first_name = fields.CharField(max_length=128, null=True)
    middle_name = fields.CharField(max_length=128, null=True)

    roles = fields.ManyToManyField('models.Role', related_name='users', through='user_role')

    class Meta:
        table = "user"
