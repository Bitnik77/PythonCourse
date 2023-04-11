# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали
# билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых
# трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.

number = input('Введите шестизначный номер билета: ')
while len(number) != 6:
    number = input('Вы ввели не корректные данные. '
                   'Введите шестизначный номер билета: ')
else:
    if int(number[0]) + int(number[1]) + int(number[2]) == int(number[3]) + int(number[4]) + int(number[5]):
        print("Ваш билет счастливый!")
    else:
        print("Ваш билет не является счастливым")
