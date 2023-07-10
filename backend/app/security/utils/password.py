from security.core.base import pwd_context


def get_password_hash(raw_password: str) -> str:
    return pwd_context.hash(raw_password)


def verify_password(hashed_password: str, plain_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)
