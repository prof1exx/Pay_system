from fastapi import Body

from main import app
from .profile_models import UserDantic, CartDantic


# Регистрация пользователя
@app.post('/api/register-user')
async def user_registration(user_data: UserDantic):
    # После регистрации выдать айди пользователя
    return {'status': 1, 'message': 'Registration completed'}


# Вход в аккаунт
@app.post('/api/login-user')
async def login_user(phone_number: int = Body(), password: str = Body()):
    print(phone_number, password)
    # Проверка данных
    checker = None

    # Если данные верны, отправляем юзер айди
    return {'status': 1, 'message': 'Logged in'}


# Добавление карты в базу
@app.post('/api/add-card')
async def add_user_card(card_data: CartDantic):
    # Вызов функции из бд для добавления карты в базу
    result = card_data
    print(card_data)

    # Если успешно добавлена карта, то status 1
    return {'status': 1, 'message': result}


# Вывод данных о пользователе
@app.get('/api/user-data')
async def get_user_data(user_id: int):
    pass


# Вывод всех или определенных карт пользователя
@app.get('/api/user-cards')
async def get_user_cards(user_id: int, card_id: int = 0):
    pass













