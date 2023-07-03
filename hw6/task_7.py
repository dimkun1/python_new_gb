# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию.

from sys import argv


__all__ = ['check_date']

_MULTIPLY_4 = 4
_MULTIPLY_100 = 100
_MULTIPLY_400 = 400


def _is_leap_year(year_val):
    if year_val % _MULTIPLY_4 != 0 or \
       year_val % _MULTIPLY_100 == 0 and year_val % _MULTIPLY_400 != 0:
        return False
    return True


def check_date(date):
    date_list = date.split(".")
    if len(date_list) != 3:
        return False
    day, mounth, year = list(map(int, date_list))
    if (len(date_list[0]) != 2 or len(date_list[1]) != 2 or len(date_list[2]) != 4):
        return False
    if not year in range(1, 10000) or not mounth in range(1, 13) or not day in range(1, 31):
        return False
    if day == 31 and mounth in [2, 4, 6, 9, 11]:
        return False
    if mounth == 2 and (day == 30 or day == 29 and _is_leap_year(year) is False):
        return False
    return True


# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.


_, input_data = argv
print(check_date(input_data))

if __name__ == "__main__":
    date = input('Введите дату для проверки: ')
    print(check_date(date))