# Задача 14
n = abs(int(input('Введите число n ')))
degree = 0
while 2 ** degree < n:
    print(2 ** degree)
    degree += 1