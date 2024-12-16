# Дано натуральное число. Напишите программу, которая вычисляет:
#
# сумму его цифр;
# количество цифр в нем;
# произведение его цифр;
# среднее арифметическое его цифр;
# его первую цифру;
# сумму его первой и последней цифры.

num = int(input())
tmp = num
tmp2 = num
tmp3 = num
tmp4 = num

sum_num = 0
lingth = 0
product = 1
first = 0

while tmp != 0:
    last_digit = tmp % 10
    sum_num += last_digit
    tmp = tmp // 10
print(sum_num)
while  num != 0:
    last_digit = num % 10
    lingth += 1
    num = num // 10
print(lingth)
while tmp2 != 0:
    last_digit = tmp2 % 10
    product *= last_digit
    tmp2 = tmp2 // 10
print(product)
print(sum_num / lingth)
while tmp3 != 0:
    last_digit = tmp3 % 10
    first = last_digit
    tmp3 = tmp3 // 10
print(first)
print(first + (tmp4 % 10))

