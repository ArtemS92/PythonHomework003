# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части

lst = list(map(float, input('Введите числа через пробел:\n').split()))
new_lst = []
for i in lst:
    if i % 1 != 0:
        new_lst.append(round(i % 1, 2))
print(max(new_lst) - min(new_lst))
