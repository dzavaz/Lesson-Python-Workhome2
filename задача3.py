# Задача 3. Счастливый билет
# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за  проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета с номером n и выводит на экран yes или no.

ticket = int(input("Введите номера Вашего билета: "))
if len(str(ticket)) !=6:
    print('Вы ввели неправильный номер билета')
else:
    n1 = ticket // 100000
    n2 = (ticket % 100000) // 10000
    n3 = (ticket % 10000) // 1000
    n4 = (ticket % 1000) // 100
    n5 = (ticket % 100) // 10
    n6 = (ticket % 10)
    if n1 + n2 + n3 == n4 + n5 + n6:
        print("Счастливый билет")
    else:
        print("Несчастливый билет")
