# Напишите для задачи 1 тесты doctest. Проверьте следующие варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)

import string
"""
Функция удаляет из текста все символы, кроме букв латинского алфавита и пробелов.
Возвращает очищенную строку в нижнем регистре.

>>> del_symbols('hello world')
'hello world'

>>> del_symbols('HeLLo WORld')
'hello world'

>>> del_symbols('hello, world!')
'hello world'

>>> del_symbols('hello Мир')
'hello '

>>> del_symbols('Hello World 123!ку')
'hello world '
"""

def del_symbols(input_text):
    """
    Функция удаляет из текста все символы, кроме букв латинского алфавита и пробелов.
    Возвращает очищенную строку в нижнем регистре.

    >>> del_symbols('hello world')
    'hello world'

    >>> del_symbols('HeLLo WORld')
    'hello world'

    >>> del_symbols('hello, world!')
    'hello world'

    >>> del_symbols('hello Мир')
    'hello '

    >>> del_symbols('Hello World 123!ку')
    'hello world '
    """
    unchecked_symbols = string.ascii_letters + ' '
    return "".join(char for char in input_text if char in unchecked_symbols).lower()

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)