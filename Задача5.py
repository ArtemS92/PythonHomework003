# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

n =int(input('Введите число: '))

neggfibb_list = []
fibb_list = []


def fibbonachi(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibbonachi(n - 1) + fibbonachi(n - 2)


for i in range(1, n + 1):
    fibb_list.append(fibbonachi(i))
    neggfibb_list.append(((-1) ** (i + 1)) * fibbonachi(i))
neggfibb_list.reverse()
neggfibb_list.append(fibb_list[0] - neggfibb_list[-1])
print(neggfibb_list + fibb_list)
