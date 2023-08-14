from database.models import User, Card
from database import get_db
from datetime import datetime
import random


def login_db(phone_number, password):
    db = next(get_db())

    checker = db.query(User).filter_by(phone_number=phone_number, password=password).first()

    if checker:
        return checker
    return False


def add_card_db(card_number, exp_date, card_name, card_balance, user_id):
    db = next(get_db())

    new_card = Card(card_number=card_number, exp_date=exp_date, card_name=card_name,
                    card_balance=card_balance, user_id=user_id, reg_date=datetime.now())

    db.add(new_card)
    db.commit()
    return new_card.id


def get_user_data_db(user_id):
    db = next(get_db())

    exact_user = db.query(User).filter_by(id=user_id).first()

    if exact_user:
        return exact_user
    return False
