# Доработайте класс прямоугольник из прошлых семинаров.
# Добавьте возможность изменять длину и ширину
# прямоугольника и встройте контроль недопустимых значений
# (отрицательных).
# Используйте декораторы свойств

# Доработаем прямоугольник и добавим экономию памяти
# для хранения свойств экземпляра без словаря __dict__.

class Rectangle:
    """Класс Прямоугольник.
    Доработан - добавлен метод сложения и вычитания по периметрам
    Добавлены методы сравнения прямоугольников по площади"""

    __slots__ = ("_side_1", "_side_2")  # доработка без словаря __dict__

    def __init__(self, side_1, side_2=0) -> None:
        self._side_1 = side_1
        if side_2 == 0:
            self._side_2 = side_1
        else:
            self._side_2 = side_2

    @property
    def side_1(self):
        return self._side_1

    @property
    def side_2(self):
        return self._side_2

    @side_1.setter
    def side_1(self, value):
        if value > 0:
            self._side_1 = value
        else:
            raise ValueError('Значение длины стороны не должно быть отрицательным')

    @side_2.setter
    def side_2(self, value):
        if value > 0:
            self._side_2 = value
        else:
            raise ValueError('Значение длины стороны не должно быть отрицательным')

    def perimeter_rectangle(self):
        return (self._side_1 + self._side_2) * 2

    def area_rectangle(self):
        return self._side_1 * self._side_2

    def __add__(self, other):
        common_p = self.perimeter_rectangle() + other.perimeter_rectangle()
        new_side_1 = max(self._side_1, self._side_2, other.side_1, other.side_2)
        new_side_2 = int((common_p - 2 * new_side_1) / 2)
        print(new_side_1, new_side_2)
        return Rectangle(new_side_1, new_side_2)

    def __sub__(self, other):
        difference = abs(self.perimeter_rectangle() -
                         other.perimeter_rectangle())
        new_side_1 = min(self._side_1, self._side_2, other.side_1, other.side_2)
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

    def __gt__(self, other) -> bool:  # больше, >
        if self.area_rectangle() > other.area_rectangle():
            return True
        return False

    def __ge__(self, other) -> bool:  # не больше, меньше или равно, <=
        if self.area_rectangle() <= other.area_rectangle():
            return True
        return False

    def __lt__(self, other) -> bool:  # меньше, <
        if self.area_rectangle() < other.area_rectangle():
            return True
        return False

    def __le__(self, other) -> bool:  # не меньше, больше или равно, >=
        if self.area_rectangle() >= other.area_rectangle():
            return True
        return False


if __name__ == "__main__":
    rect_1 = Rectangle(5, 16)
    print(rect_1.area_rectangle())
    rect_2 = Rectangle(4, 1)
    print(rect_2.area_rectangle())
    rect_1.side_1 = 8
    rect_1.side_2 = 2
    print(f'{rect_1.side_2=}')
    print(rect_1.area_rectangle())