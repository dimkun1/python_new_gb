# Задача №3 домашнего задания 4. Банкомат.

import os


def adding_funds_to_account(sum, balans, counter, DEPOSIT_BONUS, TAX_LIMIT, WEALT_TAX):
    print(f'вы пополнили счет на {sum}')
    balans += sum
    if counter < 3:
        counter += 1
    if counter == 3:
        dep_bon = round(balans * DEPOSIT_BONUS, 2)
        balans += dep_bon
        print(f'Начислены бонусы за третье пополнение счета - {dep_bon}')
        counter = 0
    if balans >= TAX_LIMIT:
        tax = round(balans * WEALT_TAX, 2)
        balans = balans - tax
        print(f'удержан налог на богатство  - {tax}')
    return balans, counter


def withdrawal_from_the_account(sum, balans, PECENT_WITHDRAWAL, PECENT_MIN, PECENT_MAX):
    if balans < sum:
        print('недостаточно средств на счете, пополните счет')
        return balans
    print(f'вы сняли {sum}')
    pecent = sum * PECENT_WITHDRAWAL
    if pecent < PECENT_MIN:
        pecent = PECENT_MIN
    if pecent > PECENT_MAX:
        pecent = PECENT_MAX
    balans -= (sum + pecent)
    print(f'удержано за снятие со счета {pecent}')
    return balans


QUOTIENT_SUM = 50
PECENT_WITHDRAWAL = 0.015
PECENT_MIN = 30
PECENT_MAX = 600
WEALT_TAX = 0.1
TAX_LIMIT = 5000000
DEPOSIT_BONUS = 0.03

if not os.path.exists('balance.txt'):
    with open('balance.txt', 'w') as f:
        f.write('0;0')

while True:
    with open('balance.txt', 'r') as f:
        str1 = f.read()

    str1 = str1.split(';')
    balans = float(str1[0])
    counter = int(str1[1])
    print(f'баланс = {balans}')
    print('выберите действие: ')
    print('пополнить - 1')
    print('снять - 2')
    print('выйти - 3')
    action = input(':')

    if action == '3':
        break

    sum = int(input('введите сумму: '))
    print('\n')
    if sum % QUOTIENT_SUM != 0:
        print(f'сума должна быть кратна {QUOTIENT_SUM}')
        continue

    if action == '1':
        balans, counter = adding_funds_to_account(sum, balans, counter, DEPOSIT_BONUS,
                                                  TAX_LIMIT, WEALT_TAX)

    if action == '2':
        balans = withdrawal_from_the_account(sum, balans, PECENT_WITHDRAWAL,
                                             PECENT_MIN, PECENT_MAX)

    balans = round(balans, 2)
    str_balans_counter = str(balans) + ';' + str(counter)

    with open('balance.txt', 'w') as f:
        f.write(str_balans_counter)

    continue