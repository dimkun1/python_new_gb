# Создайте класс прямоугольник.
# Класс должен принимать длину и ширину при создании
# экземпляра.
# У класса должно быть два метода, возвращающие периметр
# и площадь.
# Если при создании экземпляра передаётся только одна
# сторона, считаем что у нас квадрат.

class Rectangle:

    def __init__(self, side_1, side_2=0) -> None:
        self.side_1 = side_1
        if side_2 == 0:
            self.side_2 = side_1
        else:
            self.side_2 = side_2

    def perimeter_rectangle(self):
        return (self.side_1 + self.side_2) * 2

    def area_rectangle(self):
        return self.side_1 * self.side_2


class SizeError(Exception):

    def __init__(self, value) -> None:
        self.value = value

    def __str__(self) -> str:
        return f"Значение {self.value} должно быть положительным целым числом!"


if __name__ == "__main__":
    try:
        a = input('Введите длину прямоугольника: ')
        if float(a) <= 0 or not a.isdigit():
            raise SizeError(a)
        b = input('Введите ширину прямоугольника: ')
        if float(b) <= 0 or not b.isdigit():
            raise SizeError(b)
        rect = Rectangle(int(a), int(b))
    except ValueError:
        print("Создан квадрат со стороной 10")
        rect = Rectangle(10)
    print(f"P = {rect.perimeter_rectangle()}")
    print(f"S = {rect.area_rectangle()}")