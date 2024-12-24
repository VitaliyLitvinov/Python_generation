
num = int(input())
sum_fact = 0
fact = 1
while num:
    for i in range(1,num + 1):
        fact *= i
    sum_fact += fact
    fact = 1
    num -= 1
print(sum_fact)

from math import factorial

num = int(input())
sum_fact = 0
while num:
    fact = factorial(num)
    sum_fact += fact
    num -= 1
print(sum_fact)
