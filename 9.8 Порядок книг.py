# Все книги в домашней библиотеке должны быть обязательно отсортированы
# по возрастанию: сначала по фамилиям авторов, а в случае совпадения фамилий – по названиям.
# Напишите программу, которая проверяет, верно ли отсортированы книги.


flag = True
letter = ''
first_letter = ''
letter_name = ''
f_letter_name = ''
number = int(input())
for i in range(number):
    string = input()
    first_letter = string[:3]
    index_name = string.find('«') + 1
    f_letter_name = string[index_name]
    if first_letter < letter:
        flag = False
        break
    if first_letter == letter and f_letter_name < letter_name:
        flag = False
        break
    letter_name = f_letter_name
    letter = first_letter
print("YES" if flag else "NO")