from datetime import datetime

from tortoise import fields

from security.utils import password as password_logic
from models.base.base_model import CustomModel


class AbstractUser(CustomModel):
    is_staff = fields.BooleanField(default=False)
    is_active = fields.BooleanField(default=True)

    last_login = fields.DatetimeField(null=True)

    created_at = fields.DatetimeField(default=datetime.now())
    updated_at = fields.DatetimeField(null=True)

    password = fields.CharField(max_length=128)

    class Meta:
        abstract = True

    def set_password(self, raw_password: str) -> None:
        self.password = password_logic.get_password_hash(raw_password)

    def check_password(self, password: str) -> bool:
        return password_logic.verify_password(hashed_password=self.password, plain_password=password)