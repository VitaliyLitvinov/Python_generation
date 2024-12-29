# На вход программе подаётся строка текста.
# Напишите программу, которая выводит на экран символ,
# который появляется наиболее часто.

string = input()
top_letter = ''
cnt_letter = 0
for i in string:
    if string.count(i) >= cnt_letter:
        cnt_letter = string.count(i)
        top_letter = i
print(top_letter)