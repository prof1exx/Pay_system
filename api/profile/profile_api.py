from main import app
from .profile_models import UserDantic, CardDantic
from fastapi import Body
from database import profile_service


#  Регистрация пользователя
@app.post('/api/register-user')
async def user_registration(user_data: UserDantic):
    checker = profile_service.phone_number(user_data.phone_number)

    if checker:
        return {"status": 0, "message": "Номер уже зарегистрирован"}

    profile_service.register_user_db(user_data)

    return {'status': 1, 'message': 'Registration completed'}


#  Вход в аккаунт
@app.post('/api/login-user')
async def login_user(phone_number: int = Body, password: str = Body):
    checker = profile_service.login(phone_number, password)

    if checker:
        return {'status': 1, 'message': checker}

    return {"status": 0, "message": "Неправильные данные"}


#  Добавить карту
@app.post('/api/add-card')
async def add_user_card(card_data: CardDantic):

    result = profile_service.add_card_user(card_data)

    return {'status': 1, 'message': result}


#  Информация о пользователе
@app.get('/api/user-data')
async def get_user_data(user_id):
    result = profile_service.user_id_information(user_id)

    if result:
        return {'status': 1, 'message': result}

    return {"status": 0, "message": "Пользователь не найден"}


#  Карты пользователя
@app.get('/api/user-cards')
async def get_user_cards(user_id: UserDantic, card_id: CardDantic):

    result = profile_service.get_all_or_exact_card_db(user_id, card_id)

    return {'status': 1, 'message': result}
