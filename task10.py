# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

from random import randint
days = int(input('Введите кол-во монет: '))

minimum = 0
maximum = 1
count1 = 0
count2 = 0

for i in range(days):
    money = randint(minimum,maximum)
    print(money, end=' ')
    if money > 0:
        count1 += 1
    else:
        count2 += 1

print()
if count2 > count1:
    print(f'наименьшее кол-во монет чтоб перевернуть {count1} ')
else:
    print(f'наименьшее кол-во монет чтоб перевернуть {count2} ')
