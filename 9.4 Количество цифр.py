# На вход программе подаётся строка текста.
# Напишите программу, которая подсчитывает количество цифр в данной строке.

string = input()
count = 0
list_number = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
for i in range(len(string)):
    if string[i] in list_number:
        count += 1
print(count)
