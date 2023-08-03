# Напишите для задачи 1 тесты pytest. Проверьте следующие варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)

import string
import pytest

def test_no_change():
    assert del_symbols('hello world') == 'hello world', "Тест на строку без изменений провален"

def test_change_register():
    assert del_symbols('hELLo World') == 'hello world', "Тест на изменение регистра провален"

def test_del_punctuation():
    assert del_symbols('hello, world') == 'hello world', "Тест на удаление знаков препинания провален"

def test_del_other_alphabit():
    assert del_symbols('hello мир') == 'hello ', "Тест на удаление букв другого алфавита провален"

def test_all_test():
    assert del_symbols('HeLLo, Мир!') == 'hello ', "Комплексный тест провален"


def del_symbols(input_text):
    unchecked_symbols = string.ascii_letters + ' '
    return "".join(char for char in input_text if char in unchecked_symbols).lower()

if __name__ == '__main__':
    pytest.main()