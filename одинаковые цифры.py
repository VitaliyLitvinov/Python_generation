# Дано натуральное число. Напишите программу,
# которая определяет, состоит ли указанное число из одинаковых цифр.

num = int(input())
flag = True
while num > 9:
    last_digit = num % 10
    second_digit = num // 10 % 10
    if last_digit != second_digit:
        print('NO')
        flag = False
        num = 0
    num = num // 10
if flag == True:
    print('YES')