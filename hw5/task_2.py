# Задача № 2 домашнего задания 5. Однострочный генератор словаря

names = ['Андрей', 'Иван', 'Максим']
salary = [40000, 50000, 60000]
bonus = ['10.33%', '9.43%', '13.11%']
my_dict = {names[i]: round(salary[i] * float(bonus[i].replace('%', '')) / 100, 2)
           for i in range(len(names))}
print(my_dict)