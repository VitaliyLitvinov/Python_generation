# Все книги в домашней библиотеке должны быть обязательно отсортированы
# по возрастанию: сначала по фамилиям авторов, а в случае совпадения фамилий – по названиям.
# Напишите программу, которая проверяет, верно ли отсортированы книги.


n = int(input())
previous_book = ''
is_ordered = 'YES'

for i in range(n):
    s = input()
    current_surname = s[: s.find(' ')]
    current_title = s[s.find('«') + 1: s.rfind('»')]
    current_book = current_surname + current_title
    if current_book < previous_book:
        is_ordered = 'NO'

    previous_book = current_book

print(is_ordered)