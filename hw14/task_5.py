# На семинарах по ООП был создан класс прямоугольник хранящий длину и ширину,
# а также вычисляющую периметр, площадь и позволяющий складывать и вычитать прямоугольники беря за основу периметр.
# Напишите 3-7 тестов unittest для данного класса.

import unittest

from Rectangle_descriptor import Rectangle


class TestRectangle(unittest.TestCase):

    def setUp(self) -> None:
        self.for_create_test = Rectangle(2, 5)
        self.for_test_area = Rectangle(4)
        self.for_test_perimeter = Rectangle(1, 2)
        self.for_add_1 = Rectangle(4, 5)
        self.for_add_2 = Rectangle(2, 3)

    def test_create(self):
        self.assertEqual(self.for_create_test, Rectangle(2, 5), msg='Тест на создание прямоугольника провален!')


    def test_create(self):
        self.assertEqual(self.for_create_test, Rectangle(2, 5), msg='Тест на создание прямоугольника провален!')

    def test_create_error(self):
        with self.assertRaises(ValueError):
            Rectangle(-2, -5)

    def test_area(self):
        self.assertEqual(self.for_test_area.area_rectangle(), 16, msg='Тест на проверку площади провален!')

    def test_perimeter(self):
        self.assertEqual(self.for_test_perimeter.perimeter_rectangle(), 6, msg='Тест на проверку периметра провален!')

    def test_add(self):
        self.assertEqual(self.for_add_1 + self.for_add_2, Rectangle(5, (2+3+4+5)-5), msg='Тест на сложение прямоугольников провален!')

    def test_sub(self):
        self.assertEqual(self.for_add_1 - self.for_add_2, Rectangle(2, (4+5)-(2+3)-2), msg='Тест на вычитание прямоугольников провален!')



if __name__ == '__main__':
    unittest.main()