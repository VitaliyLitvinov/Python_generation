# На вход программе подаётся натуральное число n.
# Напишите программу, которая находит цифровой корень данного числа.
# Цифровой корень числа n получается следующим образом:
# если сложить все цифры этого числа, затем все цифры найденной суммы
# и повторять этот процесс до тех пор, пока в результате не будет
# получено однозначное число (цифра), которое и называется
# цифровым корнем первоначального числа n.

num = int(input())
sum_num = 0
while num:
    last_digit = num % 10
    sum_num += last_digit
    num //= 10
    if num ==0 and sum_num > 9:
        num = sum_num
        sum_num = 0
print(sum_num)

# Рекурсия
def qwer(num):
    sum_num = 0
    while num:
        last_digit = num % 10
        sum_num += last_digit
        num //= 10
    if len(str(sum_num)) > 1:
        qwer(sum_num)
    else:
        print(sum_num)

qwer(7465473856834)