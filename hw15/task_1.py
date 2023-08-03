# Напишите программу, которая использует модуль logging для
# вывода сообщения об ошибке в файл.
# Например отлавливаем ошибку деления на ноль.


import math
import logging

FORMAT = '{levelname:<8} - {asctime}. В модуле "{name}" ' \
         'в строке {lineno:03d} функция "{funcName}()" ' \
         'в {created}   {msg}'

logging.basicConfig(
    format=FORMAT, style='{', filename='./les_15/files/task_1_log.log', encoding='utf-8', level=logging.ERROR)
logger = logging.getLogger(__name__)


def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        logger.error('Деление на ноль')
        return math.inf


if __name__ == "__main__":
    print(division(8, 2))
    print(division(9, 0))