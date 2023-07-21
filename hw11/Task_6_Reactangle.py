# Доработайте прошлую задачу.
# Добавьте сравнение прямоугольников по площади
# Должны работать все шесть операций сравнения

class Rectangle:
    """Класс Прямоугольник.
    Доработан - добавлен метод сложения и вычитания по периметрам
    Добавлены методы сравнения прямоугольников по площади"""

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

    def __add__(self, other):
        common_p = self.perimeter_rectangle() + other.perimeter_rectangle()
        new_side_1 = max(self.side_1, self.side_2, other.side_1, other.side_2)
        new_side_2 = int((common_p - 2 * new_side_1) / 2)
        print(new_side_1, new_side_2)
        return Rectangle(new_side_1, new_side_2)

    def __sub__(self, other):
        difference = abs(self.perimeter_rectangle() -
                         other.perimeter_rectangle())
        new_side_1 = min(self.side_1, self.side_2, other.side_1, other.side_2)
        new_side_2 = int((difference - 2 * new_side_1) / 2)
        if new_side_2 < 0:
            new_side_1 = new_side_2 = difference / 4
        print(new_side_1, new_side_2)
        return Rectangle(new_side_1, new_side_2)

    def __eq__(self, other) -> bool:  # равно ==
        if self.area_rectangle() == other.area_rectangle():
            return True
        return False

    def __ne__(self, other) -> bool:  # не равно !=
        if self.area_rectangle() != other.area_rectangle():
            return True
        return False


if __name__ == "__main__":
    rect_1 = Rectangle(5, 16)
    print(rect_1.area_rectangle())
    rect_2 = Rectangle(4, 1)
    print(rect_2.area_rectangle())
    rect_3 = rect_1
    rect_4 = Rectangle(4, 1)

    print(rect_1 == rect_2)
    print(rect_1 == rect_3)
    print(rect_2 == rect_4)
    print()
    print(rect_1 != rect_2)
    print(rect_1 != rect_3)
    print(rect_2 != rect_4)
    print()
    print(rect_1 > rect_2)
    print(rect_1 > rect_3)
    print(rect_2 > rect_4)
    print()
    print(rect_2 < rect_1)
    print(rect_1 < rect_3)
    print(rect_2 < rect_4)
    print()
    print(rect_1 >= rect_2)
    print(rect_1 >= rect_3)
    print(rect_2 >= rect_4)
    print()
    print(rect_2 <= rect_1)
    print(rect_1 <= rect_3)
    print(rect_2 <= rect_4)