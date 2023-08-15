from main import app

import requests


# Получить курс ЦБ и нашего сервера
@app.get('/api/get-currency')
async def currency_rate():
    # Подключение к api ЦБ
    cb_api = requests.get('https://cbu.uz/ru/arkhiv-kursov-valyut/json/').json()

    # Получаем курс необходимых валют
    usd_rate = cb_api[0]['Rate']
    eur_rate = cb_api[1]['Rate']
    rub_rate = cb_api[2]['Rate']

    # Выдаем ответ
    return {'status': 1, 'rates': {'USD': usd_rate,
                                   'EUR': eur_rate,
                                   'RUB': rub_rate
                                   }}
