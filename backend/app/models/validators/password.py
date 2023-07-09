from tortoise.validators import Validator
from tortoise.exceptions import ValidationError


class PasswordValidator(Validator):
    """
    Validator for email. Email must be have '.', '@'
    """
    max_password_len: int = ...
    min_password_len: int = ...

    not_password_message: str = ''
    not_valid_password_message: str = ''
    password_must_contain_upper_message: str = ''
    password_must_contain_lower_message: str = ''
    password_must_contain_number_message: str = ''
    password_must_contain_special_message: str = ''

    class RequiredChars:
        upper: str = ''
        lower: str = ''
        numbers: str = ''
        special_chars: str = ''

    def __validate(self, password: str) -> None:
        if not password:
            raise ValidationError(self.not_password_message)

        if self.RequiredChars.upper not in password:
            raise ValidationError(self.password_must_contain_upper_message)

        if self.RequiredChars.lower not in password:
            raise ValidationError(self.password_must_contain_lower_message)

        if self.RequiredChars.numbers not in password:
            raise ValidationError(self.password_must_contain_number_message)

        if self.RequiredChars.special_chars not in password:
            raise ValidationError(self.password_must_contain_special_message)

    def __call__(self, password: str):
        self.__validate(password)
