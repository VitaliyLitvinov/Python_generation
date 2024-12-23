




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