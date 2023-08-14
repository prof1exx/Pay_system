from pydantic import BaseModel

from datetime import datetime


# Модель перевода с карты на карту
class P2PDantic(BaseModel):
    card_from: int
    amount: float
    cart_to: int
    transfer_time: datetime
