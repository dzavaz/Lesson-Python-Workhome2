# Задача 4. Площадь прямоугольного треугольника
# Прямоугольный треугольник — это треугольник, один из углов которого является прямым (90 градусов). У прямоугольного треугольника два катета,
# которые образуют прямой угол, и гипотенуза, противоположная этому углу. Вам требуется написать программу, которая запрашивает у пользователя
# длины двух катетов и выводит площадь треугольника.
# Площадь прямоугольного треугольника вычисляется по формуле: S = (1/2)a*b
# где a и b — длины катетов, а S — площадь.

cat_1 = int(input("Введите длину катета №1: "))
cat_2 = int(input("Введите длину катета №2: "))
S = 0.5*cat_1*cat_2
print(f"Площадь прямоугольника = {S}")