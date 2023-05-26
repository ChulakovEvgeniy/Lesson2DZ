# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

count = int(input('Введите степень: '))
number = 2
if count == 0:
    number = 1
else:
    for _ in range(count-1):
        number = number * number
print(number)