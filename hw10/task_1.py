# Создайте класс окружность.
# Класс должен принимать радиус окружности при создании
# экземпляра.
# У класса должно быть два метода, возвращающие длину
# окружности и её площадь.

from math import pi


class Circle:
    def __init__(self, radius) -> None:
        self.radius = radius

    def length_circle(self):
        return 2 * pi * self.radius

    def area_circle(self):
        return pi * self.radius * self.radius


if __name__ == "__main__":
    circ = Circle(5)
    print(circ.length_circle())
    print(circ.area_circle())