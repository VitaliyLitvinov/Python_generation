# На вход программе подаётся одна строка.
# Напишите программу, которая определяет,
# сколько раз в строке встречаются символы + и *, и выводит текст

counter_plus = 0
counter_multiply = 0
string = input()
for i in string:
    if i == '+':
        counter_plus += 1
    if i == '*':
        counter_multiply += 1

print('Символ + встречается',counter_plus ,'раз')
print('Символ * встречается',counter_multiply ,'раз')
