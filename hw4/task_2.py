 # Задача №2 семинара 4. Hash.

import typing


def converter_to_dict(*, a, b):
    my_dict = {}
    if isinstance(b, typing.Hashable):
        c = hash(b)
    else:
        c = str(b)
    my_dict[c] = a
    return my_dict


print('key - int:', converter_to_dict(a=1, b=2), sep='\t\t')
print('key - float:', converter_to_dict(a=1, b=2.5), sep='\t')
print('key - string:', converter_to_dict(a=1, b='2'), sep='\t')
print('key - set:', converter_to_dict(a=1, b={1, 2, 3}), sep='\t\t')
print('key - list:', converter_to_dict(a=1, b=[1, 2, 3]), sep='\t\t')
print('key - tuple:', converter_to_dict(a=1, b=(1, 2)), sep='\t')
print('key - dict:', converter_to_dict(a=1, b={1: 2}), sep='\t\t')