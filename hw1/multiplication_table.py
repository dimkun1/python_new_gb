# Задание №9 семинара 1. Таблица умножения

for i in range(2, 11):
    for j in range(2, 6):
        print(j, '*', i, '=', i * j, end='\t\t')
    print('\n')

print('\n')

for i in range(2, 11):
    for j in range(6, 10):
        print(j, '*', i, '=', i * j, end='\t\t')
    print('\n')
