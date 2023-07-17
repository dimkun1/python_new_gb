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


if __name__ == "__main__":
    rect = Rectangle(5, 16)
    print(rect.perimeter_rectangle())
    print(rect.area_rectangle())