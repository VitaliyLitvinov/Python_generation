num = int(input())
c = num % 10
b = (num % 100) // 10
a = num // 100

maxnum = max(a, b, c)
minnum = min(a, b, c)
mednum = (a + b + c) - maxnum - minnum
if maxnum - minnum == mednum:
    print('Число интересное')
else:
    print('Число неинтересное')