# Задача №3 домашнего задания 3. Рюкзак.

import itertools

MAX_WEIGHT = 10000

my_dict = {'спички': 10, 'котелок': 700, 'вода': 3000, 'ложка': 10, 'соль': 1000,
           'спальник': 3000, 'кружка': 100, 'миска': 500, 'накидка': 2, 'нож': 300,
           'фонарик': 200, 'топорик': 1500, 'одежда': 2000, 'консервы': 900, 'крупы': 2000}
my_list = []

for i in range(1, len(my_dict) + 1):
    for j in itertools.combinations(my_dict.items(), i):
        weigth_all = sum(value for _, value in j)
        if weigth_all == MAX_WEIGHT:
            my_list.append(j)

for j in my_list:
    print(j)