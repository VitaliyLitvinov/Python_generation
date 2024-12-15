num = int(input())
min_num = 10
max_num = 0
while num != 0:
    last_digit = num % 10
    if last_digit < min_num:
        min_num = last_digit
    if last_digit > max_num:
        max_num = last_digit
    num = num // 10
print('Максимальная цифра равна', max_num)
print('Минимальная цифра равна', min_num)