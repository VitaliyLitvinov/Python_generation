from math import sqrt
a = float(input())
b = float(input())
c = float(input())
dis = b**2 - 4*a*c
if dis == 0:
    print(-b / (2*a))

elif dis > 0:
    x1 = (-b - sqrt(dis)) / (2*a)
    x2 = (-b + sqrt(dis)) / (2*a)
    print(min(x1, x2))
    print(max(x1, x2))
else:
    print('Нет корней')