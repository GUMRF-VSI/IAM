from config.security.core.base import pwd_context


class PasswordLogic:
    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def get_password_hash(raw_password: str) -> str:
        return pwd_context.hash(raw_password)


password = PasswordLogic()
