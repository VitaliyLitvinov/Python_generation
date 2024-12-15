num = int(input())
reverse_num = ''
while num != 0:
    last_digit = num % 10
    reverse_num += str(last_digit)
    num = num // 10
print(reverse_num)