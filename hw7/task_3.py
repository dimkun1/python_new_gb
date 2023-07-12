# Напишите функцию, которая открывает на чтение созданные
# в прошлых задачах файлы с числами и именами.
# Перемножьте пары чисел. В новый файл сохраните
# имя и произведение:
# если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
# если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
# В результирующем файле должно быть столько же строк, сколько в более длинном файле.
# При достижении конца более короткого файла,
# возвращайтесь в его начало.

__all__ = ['gen_common_file']


def gen_common_file(name_file_1, name_file_2):
    with (
        open(name_file_1, 'r', encoding='utf-8') as names, \
            open(name_file_2, 'r', encoding='utf-8') as numbers, \
            open("./files/task_3/total_file", 'w+', encoding='utf-8') as total
    ):
        len_numbers = sum(1 for _ in numbers)
        len_names = sum(1 for _ in names)
        max_len = max(len_numbers, len_names)
        names.seek(0, 0)
        numbers.seek(0, 0)
        print(len_names, len_numbers, max_len)
        count = 0
        while count < max_len:
            for name, num in zip(names, numbers):
                num_mult = float(num.split('|')[0]) * float(num.split('|')[1])
                if num_mult < 0:
                    total.write(f"{name.lower().strip()} {abs(num_mult)}\n")
                else:
                    total.write(f"{name.upper().strip()} {int(num_mult)}\n")
                count += 1
                if count == len_numbers and count <= len_names:
                    numbers.seek(0, 0)
                elif count == len_names and count <= len_numbers:
                    names.seek(0, 0)


if __name__ == "__main__":
    gen_common_file("./files/task_2/letters.txt", "./files/task_1/numbers.txt")