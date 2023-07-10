# Напишите функцию, которая генерирует
# псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.
from random import choice, randint, sample

__all__ = ['name_gen']

MIN_LEN = 4
MAX_LEN = 7
VOWEL_LETTERS = 'eyuioa'
CONSONANT_LETTERS = 'qwrtpsdfghjklzxcvbnm'
INPUT_ROW = 5


def name_gen(quntity_strings: int, name_file: str):
    with open(name_file, mode='a', encoding='utf-8') as f:
        new_name = ""
        for _ in range(quntity_strings):
            quantity_vowel = randint(1, MIN_LEN - 1)
            quantity_consonant = randint(1, MAX_LEN - quantity_vowel)
            for i in range(quantity_vowel):
                new_name = new_name + choice(VOWEL_LETTERS)
            for i in range(quantity_consonant):
                new_name = new_name + choice(CONSONANT_LETTERS)
            sample(new_name, 1)
            f.write(f"{new_name.capitalize()}\n")
            new_name = ""


if __name__ == "__main__":
    name_gen(INPUT_ROW, "./files/task_2/letters.txt")
