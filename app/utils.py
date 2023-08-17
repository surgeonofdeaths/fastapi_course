from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_hash(password: str) -> str:
    new_password = pwd_context.hash(password)
    print(new_password, type(new_password))
    return new_password
