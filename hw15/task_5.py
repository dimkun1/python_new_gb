# Дорабатываем задачу 4.
# Добавьте возможность запуска из командной строки.
# При этом значение любого параметра можно опустить.
# В этом случае берётся первый в месяце день недели, текущий день недели и/или текущий месяц.

# *Научите функцию распознавать не только текстовое названия дня недели и месяца, но и числовые,
# т.е не мая, а 5.

from task_4 import convert_date
import argparse
from datetime import datetime


def pars_date():
    parser = argparse.ArgumentParser(prog="Работа с датой")
    parser.add_argument('-d', metavar='d', default='1-й')
    parser.add_argument('-w', metavar='w', default=datetime.now().weekday())
    parser.add_argument('-m', metavar='m', default=datetime.now().month)
    args = parser.parse_args()
    return convert_date(f'{args.d} {args.w} {args.m}')


if __name__ == "__main__":
    print(pars_date())