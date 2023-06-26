# Задача №6 семирара. Сумма среза списка.

def sum_list(lst, min_index, max_index):
    sum_lst = sum(lst[min_index: max_index])
    return sum_lst


print(sum_list([1, 2, 3, 4, 5, 6, 7, 8], 3, 7))