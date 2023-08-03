# Напишите для задачи 1 тесты unittest. Проверьте следующие варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)

import string
import unittest


class TestCaseName(unittest.TestCase):
    def test_no_change(self):
        self.assertEqual('hello world', del_symbols('hello world'), msg='Тест провален')

    def test_change_register(self):
        self.assertEqual('hello world', del_symbols('HeLLo WORld'), msg='Тест провален')

    def test_del_punctuation(self):
        self.assertEqual('hello world', del_symbols('hello, world'), msg='Тест провален')

    def test_del_other_alphabit(self):
        self.assertEqual('hello ', del_symbols('hello мир'), msg='Тест провален')

    def test_all_test(self):
        self.assertEqual('hello ', del_symbols('HeLLo, Мир!'), msg='Тест провален')


def del_symbols(input_text):
    unchecked_symbols = string.ascii_letters + ' '
    return "".join(char for char in input_text if char in unchecked_symbols).lower()


if __name__ == '__main__':
    unittest.main()