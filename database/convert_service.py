from database.models import PayCategory
from database import get_db


# функция получение курс ЦБ и нашего сервиса
def exchange_rates(category_name):
    db = next(get_db())

    exact_user_info = db.query(PayCategory).filter_by(id=category_name).first()

    if exact_user_info:
        return exact_user_info

    return 'Ошибка в данных'
