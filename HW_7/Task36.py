# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть
# распечатаны. Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как,
# например, у операции умножения.

m = int(input('Введите число: '))
n = int(input('Введите число: '))


def operation(x, y):
    for i in range(1, x + 1):
        for j in range(1, y + 1):
            print("%4d" % (i * j), end='')
        print()


def print_operation_table(operation, num_rows=6, num_columns=6):
    return operation(num_rows, num_columns)


print_operation_table(operation, m, n)
