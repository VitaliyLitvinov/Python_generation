num = int(input())
sum_num = 0
linght_num = 1
product = 1
mean = 0
f_dig = 0
sum_f_a_l = 0
while num != 0:
    last_digit = num % 10
    sum_num += last_digit
    num = num // 10
print(sum_num)
while num != 0:
    last_digit = num % 10
    linght_num = linght_num + 1
    num = num // 10
print(linght_num)
while num != 0:
    last_digit = num % 10
    product *= last_digit
    num = num // 10
print(product)
print(sum_num / linght_num)
while num != 0:
    last_digit = num % 10
    f_dig = last_digit
    num = num // 10
print(f_dig)
print(f_dig + (num % 10))