# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат
# заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

lst = [random.randint(-50, 50) for _ in range(int(input(
    'Введите количество элементов в списке: ')))]
print(*lst)
minLst = int(input(
    'Введите минимальное значение диапазона: '))
maxLst = int(input(
    'Введите максимальное значение диапазона: '))


def func():
    for i in lst:
        if minLst <= i <= maxLst:
            print(lst.index(i), end=' ')


func()
