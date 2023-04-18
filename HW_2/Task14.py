# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2**k), не превосходящие числа N.
'''
number = int(input("Введите число: "))
i = 0
for i in range(number):
    if 2 ** i < number:
        print(2 ** i, end=" ")
'''
# Или решение с помощью библиотеки
import math

number = int(input("Введите число: "))
for i in range(number):
    k = pow(2, i)
    if k < number:
        print(k)
