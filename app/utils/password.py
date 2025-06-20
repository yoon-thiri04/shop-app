from passlib.context import CryptContext

pwd_content = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash(password:str):
    return pwd_content.hash(password)

def verify(plain_password:str, hashed_password: str):
    return pwd_content.verify(plain_password, hashed_password)