# Создайте класс Матрица. Добавьте методы для:
# ○ вывода на печать,
# ○ сравнения,
# ○ сложения,
# ○ *умножения матриц

from random import randint as rnd


class Matrix:
    __UP_LEVEL_VALUE = 10
    __DOWN_LEVEL_VALUE = -10

    __UP_LEVEL_SIZE = 10
    __DOWN_LEVEL_SIZE = 1

    def __init__(self, *args) -> None:
        if len(args) == 1:
            if isinstance(*args, list):
                self.value = list(*args)
                self.length = len(self.value)
                self.heigth = len(self.value[0])
            else:
                self.length = self.heigth = int(*args)
                self.value = [[rnd(self.__DOWN_LEVEL_VALUE, self.__UP_LEVEL_VALUE)
                               for _ in range(self.heigth)] for _ in range(self.length)]
        elif len(args) == 2:
            self.length = args[0]
            self.heigth = args[1]
            self.value = [[rnd(self.__DOWN_LEVEL_VALUE, self.__UP_LEVEL_VALUE)
                           for _ in range(self.heigth)] for _ in range(self.length)]
        else:
            self.length = rnd(self.__DOWN_LEVEL_SIZE,
                              self.__UP_LEVEL_SIZE)
            self.heigth = rnd(self.__DOWN_LEVEL_SIZE,
                              self.__UP_LEVEL_SIZE)
            self.value = [[rnd(self.__DOWN_LEVEL_VALUE, self.__UP_LEVEL_VALUE)
                           for _ in range(self.heigth)] for _ in range(self.length)]

    def __str__(self) -> str:
        return "\n".join(str(i) for i in self.value)


    def is_eq_size(self, other) -> bool:
        if self.length == other.length\
                and self.heigth == other.heigth:
            return True
        else:
            return False

    def __eq__(self, other) -> bool:
        """Матрицы равны, если они одинакового размера
        и все их элементы на одинковых позициях равны"""
        if self.is_eq_size(other):
            for i, j in zip(self.value, other.value):
                if i != j:
                    return False
        else:
            return False
        return True

    def __ne__(self, other) -> bool:
        """Матрицы равны, если они разного размера
        или есть хотя бы одна пара неравных элементов на одинковых позициях"""
        if self.is_eq_size(other) is False:
            return True
        else:
            for i, j in zip(self.value, other.value):
                if i != j:
                    return True
        return False

    def __gt__(self, other) -> bool:
        """Матрица больше другой, если обе матрицы одинакового размера
        и все элементы первой матрицы больше элементов другой матрицы
        на одинковых позициях"""
        temp = self.__sub__(other)
        for string in temp.value:
            for elem in string:
                if elem < 0:
                    return False
        if self.__eq__(other) is True:
            return False
        return True

    def __ge__(self, other) -> bool:
        """Матрица больше или равна другой, если обе матрицы одинакового размера
        и все элементы первой матрицы больше или равны элементам другой матрицы
        на одинковых позициях"""
        temp = self.__sub__(other)
        for string in temp.value:
            for elem in string:
                if elem < 0:
                    return False
        return True

    def __lt__(self, other) -> bool:
        """Матрица меньше другой, если обе матрицы одинакового размера
        и все элементы первой матрицы меньше элементов другой матрицы
        на одинковых позициях"""
        temp = self.__sub__(other)
        for string in temp.value:
            for elem in string:
                if elem > 0:
                    return False
        if self.__eq__(other) is True:
            return False
        return True

    def __le__(self, other) -> bool:
        """Матрица меньше или равна другой, если обе матрицы одинакового размера
        и все элементы первой матрицы меьше или равны элементам другой матрицы
        на одинковых позициях"""
        temp = self.__sub__(other)
        for string in temp.value:
            for elem in string:
                if elem > 0:
                    return False
        return True

    def __add__(self, other):
        result_matrix = []
        if self.is_eq_size(other):
            for i, j in zip(self.value, other.value):
                string = [elem_i + elem_j for elem_i, elem_j in zip(i, j)]
                result_matrix.append(string)
        else:
            raise ValueError(f"Матрицы имеют разную размерность!")
        return Matrix(result_matrix)

    def __sub__(self, other):
        result_matrix = []
        if self.is_eq_size(other):
            for i, j in zip(self.value, other.value):
                string = [elem_i - elem_j for elem_i, elem_j in zip(i, j)]
                result_matrix.append(string)
        else:
            raise ValueError(f"Матрицы имеют разную размерность!")
        return Matrix(result_matrix)

    def __mul__(self, other):
        result_matrix = []
        if self.length != other.heigth\
                and self.heigth != other.length:
            raise ValueError(f"Матрицы имеют разную размерность!")
        elif self.heigth == other.length:
            common_size = self.heigth
            first_value = self.value
            second_value = other.value
            first_size = self.length
            second_size = other.heigth
        else:
            common_size = self.length
            first_value = other.value
            second_value = self.value
            first_size = other.length
            second_size = self.heigth
        for i in range(first_size):
            temp_string = []
            for j in range(second_size):
                elem = sum(first_value[i][p] * second_value[p][j]
                           for p in range(common_size))
                temp_string.append(elem)
            result_matrix.append(temp_string)
        return Matrix(result_matrix)


if __name__ == "__main__":
    m_1 = Matrix([[3, 0, 2], [1, 1, 2], [2, 2, 3]])
    m_2 = Matrix([[3, 3, 3], [1, 9, 1], [1, 1, 1]])
    m_3 = Matrix()
    m_4 = Matrix(5)
    m_5 = Matrix(3,2)
    m_6 = Matrix(2, 8, [[3, 3, 3], [1, 9, 1], [1, 1, 1]])
    m_7 = Matrix([[3, 3, 3], [1, 9, 1], [1, 1, 1]])
    print("Матрица 1")
    print(m_1)
    print("Матрица 2")
    print(m_2)
    print("Матрица 3")
    print(m_3)
    print("Матрица 4")
    print(m_4)
    print("Матрица 5")
    print(m_5)
    print("Матрица 6")
    print(m_6)
    print("Сумма матриц 1 и 2")
    print(m_1 + m_2)
    print("Произведение матриц 1 и 5")
    print(m_1 * m_5)
    print(m_2 == m_7)
    print(m_1 < m_2)