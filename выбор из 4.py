# Напишите программу, которая определяет наименьшее из четырёх чисел.
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a < b:
    min_ab = a
else:
    min_ab = b
if c < d:
    min_cd = c
else:
    min_cd = d
if min_ab < min_cd:
    print(min_ab)
else:
    print(min_cd)