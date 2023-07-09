from tortoise.validators import Validator
from tortoise.exceptions import ValidationError


class EmailValidator(Validator):
    message = "Enter a valid email address."

    def __validate(self, email: str) -> None:
        if not email or "@" not in email or len(email) > 320:
            raise ValidationError(self.message)

    def __call__(self, email: str):
        self.__validate(email)
