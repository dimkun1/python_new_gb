# Добавьте в модуль с загадками функцию, которая принимает на вход строку (текст загадки) и число (номер попытки, с которой она угадана).
# Функция формирует словарь с информацией о результатах отгадывания.
# Для хранения используйте защищённый словарь уровня модуля.
# Отдельно напишите функцию, которая выводит результаты угадывания из защищённого словаря в удобном для чтения виде.
# Для формирования результатов используйте генераторное выражение.

__all__ = ['some_riddles', 'print_dictionary_answer']

QUATITY_TRY = 3


def riddle(text, list_of_key):
    print(text)
    for i in range(QUATITY_TRY):
        answer = input(f"У Вас {QUATITY_TRY} попыток. Введите Ваш ответ:")
        if answer in list_of_key:
            print(f"Вы угадали с {i + 1} попытки!")
            return i + 1
        else:
            print(f"неверно! {text}")
    return 0


def some_riddles():
    dict_riddle = {"Зимой и летом одним цветом": ["Ёлка", "елка", "ёлка", "Елка", "ель", "Ель"], \
                   "Не расческа, а свистит": ["Свисток", "Свист", "свисток"],
                   "Не ведро, а гавкает": ["Собака", "пес", "Щенок"]}
    _dictionary_answer = {form_dict(rid, riddle(rid, answ)) for rid, answ in dict_riddle.items()}
    return (_dictionary_answer)


def form_dict(text_of_riddle, answer_riddle):
    _dictionary_answer[text_of_riddle] = answer_riddle


def print_dictionary_answer():
    for key, val in _dictionary_answer.items():
        print(f'Загадка "{key}" отгадана с {val} попытки\n')


_dictionary_answer = {}

if __name__ == "__main__":
    some_riddles()
    print_dictionary_answer()
