# Задача №2 домашнего задания 3. 10 самых популярных слов из статьи.

import string

MAX_QUANTITY = 10
my_dict = {}
counter = 0
with open('text.txt', 'r') as f:
    my_text = f.read()

my_text = my_text.translate(str.maketrans('', '', string.punctuation))
my_text = my_text.lower()
my_text = my_text.split()

for item in my_text:
    my_dict[my_text.count(item)] = item

sorted_dict = dict(sorted(my_dict.items(), reverse=True))

for item, value in sorted_dict.items():
    if counter < MAX_QUANTITY:
        print(item, '\t', value)
        counter += 1