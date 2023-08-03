# На семинаре про декораторы был создан логирующий
# декоратор. Он сохранял аргументы функции и результат её
# работы в файл.
# Напишите аналогичный декоратор, но внутри используйте
# модуль logging.

# Доработаем задачу 2.
# Сохраняйте в лог файл раздельно:
# ○ уровень логирования, levelname
# ○ дату события, asctime
# ○ имя функции (не декоратора), function_,__name__
# ○ аргументы вызова, args
# ○ результат. result


from typing import Callable
import logging


def logger(function_: Callable):

    FORMAT = '{levelname} - {asctime} <<{msg}>>'
    logging.basicConfig(
        format=FORMAT, style='{', filename='./les_15/files/task_2_log.log', encoding='utf-8', level=logging.INFO)
    logger = logging.getLogger(__name__)

    def wrapper(*args, **kwargs):
        result = function_(*args, **kwargs)
        logger.info(
            f"{function_.__name__} Коэффициенты: {args}, Корни: {result}")
    return wrapper


@logger
def root_quadratic_equation(*args):
    a, b, c = args
    d = b ** 2 - 4 * a * c
    if a != 0:
        x_1 = (-b + d ** 0.5) / 2 / a
        x_2 = (-b - d ** 0.5) / 2 / a
    elif b != 0:
        x_1 = x_2 = -c / b
    else:
        x_1 = x_2 = "нет корней"
    return x_1, x_2


if __name__ == "__main__":
    root_quadratic_equation(4, 2, -3)