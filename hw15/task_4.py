# Функция получает на вход текст вида: “1-й четверг ноября”, “3-я среда мая” и т.п.
# Преобразуйте его в дату в текущем году.
# Логируйте ошибки, если текст не соответсвует формату.

import logging
from datetime import date, datetime

FORMAT = '{levelname} - {asctime}.' \
         'в строке {lineno:03d} функция "{funcName}()" ' \
         'в {created}   {msg}'

logging.basicConfig(
    format=FORMAT, style='{', filename='./files/task_4_log.log', encoding='utf-8', level=logging.ERROR)
logger = logging.getLogger(__name__)


def convert_date(string_date):
    days_dict = {'понедельник': 0, 'вторник': 1, 'среда': 2,
                 'четверг': 3, 'пятница': 4, 'суббота': 5, 'воскресенье': 6}
    mounth_dict = {'января': 1, 'февраля': 2, 'марта': 3, 'апреля': 4, 'мая': 5, 'июня': 6,
                   'июля': 7, 'августа': 8, 'сентября': 9, 'октября': 10, 'ноября': 11, 'декабря': 12}
    try:
        count_day, day_, mounth_ = string_date.split()
        count_day = int(count_day[0])
        if day_.isdigit():  # для распознавания числового формата
            day_ = int(day_) - 1
        else:
            day_ = days_dict[day_]
        if mounth_.isdigit():  # для распознавания числового формата
            mounth_ = int(mounth_)
        else:
            mounth_ = mounth_dict[mounth_]
        count = 1
        for i in range(1, 32):
            date_ = date(year=datetime.now().year, month=mounth_, day=i)
            if date_.weekday() == day_ and count == count_day:
                return date_
            elif date_.weekday() == day_ and count < count_day:
                count += 1
        raise ValueError('Неверный формат ввода')
    except Exception:
        logger.error(f"Текст не соответствует формату - {string_date}")


if __name__ == "__main__":
    print(convert_date("1-й 10 14"))