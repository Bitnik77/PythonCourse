# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты
# вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

import random

count = count1 = 0
number = int(input("Введите количество монеток: "))
for _ in range(number):
    coin = random.randint(0, 1)
    print(coin, end=" ")
    if coin == 0:
        count += 1
    else:
        count1 += 1

print()

if count > count1:
    print(count1)
else:
    print(count)
