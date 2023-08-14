from main import app
from .transfers_models import P2PDantic


# Запрос на перевод денег между картами
@app.post('/api/transfer-money')
async def money_transfer(transfer_data: P2PDantic):
    # Функция перевода денег
    result = transfer_data
    print(result)

    # Если перевод успешный, то status: 1
    return {'status': 1, 'message': result}


# Функция получения последних транзакций пользователя
@app.get('/api/monitoring')
async def user_payments(user_id: int, card_id: int = 0):
    pass


















