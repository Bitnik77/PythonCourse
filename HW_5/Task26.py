# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А
# в целую степень B с помощью рекурсии.

def degree(a, b):
    if b == 1:
        return a
    return a * degree(a, b - 1)


a = int(input('Введите число А: '))
b = int(input('Введите число В: '))

print(degree(a, b))
