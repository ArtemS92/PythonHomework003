# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.

from random import *

n = int(input('Введите размер списка: '))
some_list = []
summ = 0
a = int(input('Введите диапазон чисел\nОт a: '))
b = int(input('До b: '))
for i in range(0, n):
    some_list.append(randint(a, b))
    if i % 2 != 0:
        summ += some_list[i]

print(some_list)
print(f'Сумма элементов, стоящих на нечетной позиции равна {summ}')