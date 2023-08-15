from database import Base
from sqlalchemy import Column, String, BigInteger, DateTime, Float, ForeignKey, Integer
from sqlalchemy.orm import relationship


# Таблица пользователей
class User(Base):
    __tablename__ = 'users'
    id = Column(BigInteger, autoincrement=True, primary_key=True)
    profile_photo = Column(String)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    phone_number = Column(BigInteger, nullable=False)
    email = Column(String, nullable=False)
    city = Column(String)
    reg_date = Column(DateTime)
    password = Column(String, nullable=False)


# Таблица карт
class Card(Base):
    __tablename__ = 'cards'
    id = Column(BigInteger, autoincrement=True, primary_key=True)
    user_id = Column(BigInteger, ForeignKey('users.id'), nullable=False)
    card_number = Column(BigInteger, nullable=False, unique=True)
    expire_date = Column(Integer, nullable=False)
    card_balance = Column(Float, default=15000)
    card_name = Column(String, default='My card')

    reg_date = Column(DateTime)

    user_fk = relationship(User, lazy='subquery')


# Таблица платежей
class Transactions(Base):
    __tablename__ = 'user_transaction'
    id = Column(BigInteger, autoincrement=True, primary_key=True)
    card_from = Column(BigInteger, ForeignKey('cards.card_number'))
    amount = Column(Float)
    card_to = Column(BigInteger, ForeignKey('cards.card_number'))
    transfer_time = Column(DateTime)

    card_from_fk = relationship(Card, lazy='subquery')
    card_to_fk = relationship(Card, lazy='subquery')


# Таблица категорий платежей
class PayCategory(Base):
    __tablename__ = 'pay_categories'
    id = Column(BigInteger, autoincrement=True, primary_key=True)
    category_name = Column(String, nullable=False)

    reg_date = Column(DateTime)
