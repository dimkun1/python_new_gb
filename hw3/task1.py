# Задача №1 домашнего задания 3. Вернуть список с дублирующимися элементами.

my_list = [1, 2, 4, 9, 2, 9, 10, 11, 12, 35, 1, 2, 35, 35, 80]
my_list_d = []

for item in my_list:
    if my_list.count(item) > 1 and item not in my_list_d:
        my_list_d.append(item)

print(f'Первоначальный список: {my_list}')
print(f'Список дублирующихся элементов: {my_list_d}')