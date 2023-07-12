from random import randint as rnd

__all__ = ['common_check', 'print_board', 'all_solutions']

_SIZE = 8
_COUNT_OPTION = 4

# Добавьте в пакет, созданный на семинаре шахматный модуль.
# Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.


def _check_dangerous(pos_queen: list) -> bool:
    size = len(pos_queen)
    for i, point in enumerate(pos_queen):
        for j in range(i+1, size):
            if point[0] == pos_queen[j][0] \
            or point[1] == pos_queen[j][1] \
            or abs(point[0] - pos_queen[j][0]) == abs(point[1] - pos_queen[j][1]):
                return False
    return True


def _check_size(pos_queen: list) -> bool:
    size = len(pos_queen)
    if size != _SIZE:
        return False
    for i, point in enumerate(pos_queen, start=1):
        if i > _SIZE:
            return False
        if len(point) != 2:
            return False
        if not (point[0] or point[1]) in range(1,_SIZE+1):
            return False
    return True


def common_check(pos_queen):
    if _check_dangerous(pos_queen) and _check_size(pos_queen):
        return True
    return False

# Напишите функцию в шахматный модуль.
# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
# Проверяйте различные случайные варианты и выведите 4 успешных расстановки.
# *Выведите все успешные варианты расстановок


def _put_place_queen(new_column, pos_queen, total_solution):
    if len(pos_queen) == _SIZE:
        total_solution.append(tuple(pos_queen))
    else:
        for new_row in range(1, _SIZE+1):
            if _no_dangerous((new_column, new_row), pos_queen):
                _put_place_queen(new_column+1, pos_queen+[(new_column, new_row)], total_solution)


def _no_dangerous(new_point, pos_queen):
    for point in pos_queen:
        if point[0] == new_point[0] or point[1] == new_point[1] or \
        abs(point[0] - new_point[0]) == abs(point[1] - new_point[1]):
            return False
    return True


def print_board(total_solution):
    for _ in range(_COUNT_OPTION):
        print_instance = rnd(0,len(total_solution)-1)
        print(f"Случайное решение - {print_instance}")
        for queen in total_solution[print_instance]:
            print(f'{". "*(queen[1]-1)+"X "+". "*(_SIZE-queen[1])}')


def all_solutions(total_solution):
    for i in range(1, _SIZE+1):
        for j in range(1, _SIZE+1):
            _put_place_queen(2, [(i, j)], total_solution)
    return total_solution


if __name__ == "__main__":
    total_solution = []
    all_solutions(total_solution)
    print("Все возможные комбинации:")
    for i, item in enumerate(total_solution):
        print(f"{i} - {item} - {common_check(item)}")
    print_board(total_solution)