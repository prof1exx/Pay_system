from pydantic import BaseModel

from datetime import datetime


# Модель входных данных пользователя
class UserDantic(BaseModel):
    user_id: int
    profile_photo: str
    name: str
    surname: str
    phone_number: int
    email: str
    city: str
    reg_date: datetime
    password: str


# Модель для карты пользователя
class CardDantic(BaseModel):
    number: int
    holder: str
    expiry_date: int
    balance: float
    name: str

