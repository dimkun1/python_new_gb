#Задача про транспонирование матриц

class BaseException(Exception):
    pass


class SizeMatrixError(BaseException):
    def __init__(self, value, size) -> None:
        self.value = value
        self.size = size

    def __str__(self) -> str:
        return f"Количество вводимых значений должно быть равно {self.size}! Вы ввели {len(self.value)} значения(й)!"


class FormatSizeError(BaseException):
    def __init__(self, index, value) -> None:
        self.value = value
        if index == 0:
            self.size = "длины"
        else:
            self.size = "высоты"


class ValueMatrixError(BaseException):
    def __init__(self, index, value) -> None:
        self.value = value
        self.index = index

    def __str__(self) -> str:
        return f'В качестве элементов матрицы необходимо ввести целые числа через пробел. \
Вы ввели "{self.value}" в качестве {self.index + 1} элемента строки!'


def transopse_matrix(list_matrix: list) -> list:
    return_matrix = []
    for item in zip(*list_matrix):
        return_matrix.append(list(item))
    return return_matrix


def print_matrix(list_matrix: list):
    for i in range(len(list_matrix)):
        print(list_matrix[i])


def input_matrix(length_matrix: int, weigth_matrix: int) -> list:
    list_matrix = []
    for i in range(weigth_matrix):
        string_matrix = list(input(
            f"Введите {length_matrix} элемента(ов) {i+1} строки через пробел: ").split())
        if len(string_matrix) != length_matrix:
            raise SizeMatrixError(string_matrix, length_matrix)
        for i, elem in enumerate(string_matrix):
            if not elem.isdigit():
                raise ValueMatrixError(i, elem)
            else:
                string_matrix[i] = int(elem)
        list_matrix.append(list(string_matrix))
    return list_matrix


if __name__ == "__main__":
    value = (input("Введите длину и высоту матрицы через пробел: ").split())
    if len(value) != 2:
        raise SizeMatrixError(value, 2)
    for i, elem in enumerate(value):
        if not elem.isdigit():
            raise FormatSizeError(i, elem)
    length, weigth = map(int, value)

    matrix = input_matrix(length, weigth)
    print("Введенная матрица:")
    print_matrix(matrix)
    new_matrix = transopse_matrix(matrix)
    print("Транспонированная матрица:")
    print_matrix(new_matrix)