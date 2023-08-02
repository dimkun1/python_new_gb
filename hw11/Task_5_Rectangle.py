# Дорабатываем класс прямоугольник из прошлого семинара.
# Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр прямоугольника.
# Складываем и вычитаем периметры, а не длинну и ширину.
# При вычитании не допускайте отрицательных значений


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


if __name__ == "__main__":
    rect_1 = Rectangle(3, 2)
    print(rect_1.perimeter_rectangle())
    print()
    # print(rect_1.area_rectangle())
    rect_2 = Rectangle(2, 2)
    print(rect_2.perimeter_rectangle())
    print()
    # print(rect_2.area_rectangle())
    s = rect_1 + rect_2
    print(s.perimeter_rectangle())
    print(s.area_rectangle())
    print()
    d = rect_1 - rect_2
    print(d.perimeter_rectangle())
    print(d.area_rectangle())


# class Rectangle:
#     def __init__(self, *args):
#         if len(args) == 1:
#             self.length = args[0]
#             self.width = self.length
#         else:
#             self.length, self.width = args

#     def get_perimeter(self):
#         return self.length * 2 + self.width * 2

#     def get_square(self):
#         return self.length * self.width

#     def get_perimeters(self, other):
#         return self.length * 2 + self.width * 2, other.length * 2 + other.width * 2

#     def __add__(self, other):
#         sum_perimeters = sum(self.get_perimeters(other))
#         print(sum_perimeters)
#         min_size = min(self.width, self.length, other.width, other.length)
#         two_size = (sum_perimeters - min_size * 2) / 2
#         return Rectangle(min_size, two_size)

#     def __sub__(self, other):
#         p_1, p_2 = self.get_perimeters(other)
#         sub_perimeters = abs(p_1 - p_2)
#         size = sub_perimeters / 4
#         return Rectangle(size)
# if __name__ == '__main__':
#     rec_1 = Rectangle(5)
#     rec_2 = Rectangle(5, 7)
#     sum_rec = rec_1 + rec_2
#     print(sum_rec.length, sum_rec.width)
#     sub_rec = rec_1 - rec_2
#     print(sub_rec.length, sub_rec.width)