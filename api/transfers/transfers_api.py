from main import app
from .transfers_models import P2PDantic
from database import transfer_service


@app.post('/api/transfer-money')
async def money_transfer(transfer_data: P2PDantic):
    result = transfer_service.money_transfer_db(transfer_data)

    if result:
        return {'status': 1, 'message': result}

    return {'status': 0, 'message': "Ошибка перевода"}


@app.get('/app/monitoring')
async def user_payments(user_id: int):
    history = transfer_service.get_card_history(user_id)

    return {'status': 1, 'message': history}
