# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов
# второго множества. Затем пользователь вводит сами элементы множеств.

import random

n = int(input('Введите количество элементов в первом множестве: '))
m = int(input('Введите количество элементов во втором множестве: '))

set1 = {random.randint(-10, 10) for _ in range(n)}
set2 = {random.randint(-10, 10) for _ in range(m)}

print(*set1)
print(*set2)

set3 = set1.intersection(set2)

print(*set3)
list1 = list(set3)
temp = 0

for i in range(len(list1) - 1):  # вместо ручного перебора метод sort()
    for i in range(len(list1) - 1):  # list1.sort()
        if list1[i] > list1[i + 1]:  #
            temp = list1[i]          #
            list1[i] = list1[i + 1]  #
            list1[i + 1] = temp      #

print(*list1)
