# программа выводит вторую цифру

num = int(input())
while num > 9 :
    last_digit = num % 10
    second = last_digit
    num = num // 10
print(second)