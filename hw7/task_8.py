# Напишите функцию группового переименования файлов. Она должна:
# ✔ принимать параметр желаемое конечное имя файлов.+
# При переименовании в конце имени добавляется порядковый номер.+
# ✔ принимать параметр количество цифр в порядковом номере.+
# ✔ принимать параметр расширение исходного файла. +
# Переименование должно работать только для этих файлов внутри каталога. +
# ✔ принимать параметр расширение конечного файла.+
# ✔ принимать диапазон сохраняемого оригинального имени. Например для диапазона
# [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется
# желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.

from os import listdir, rename, path, getcwd

__all__ = ['group_rename']


def group_rename(begin_extention, final_extention, range_of_begin_sym=[0, 0], final_name="", len_count=2):
    count = 1
    for file in listdir(getcwd()):
        if path.isfile(file) and file.split(".")[-1] == begin_extention:
            old_chars = ""
            max_limit = min(max(range_of_begin_sym), len(file.split(".")[0]))
            min_limit = min(range_of_begin_sym)
            if min_limit >= max_limit:
                min_limit = max_limit
            elif min_limit < 0:
                min_limit = 0
            for i in range(min_limit, max_limit):
                old_chars = old_chars+file[i]
            len_zero = max(0, len_count - len(str(count)))
            new_name = old_chars + final_name + len_zero * \
                "0" + str(count) + "." + final_extention
            rename(file, new_name)
            count += 1


if __name__ == "__main__":
    group_rename("txt", "csv", [200, 100], "final")