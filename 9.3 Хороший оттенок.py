# На вход программе подаётся строка текста.
# Напишите программу, которая определяет, является ли оттенок текста хорошим или нет.
# Текст имеет хороший оттенок, если содержит подстроку «хорош»
# (без кавычек) во всевозможных регистрах.

string = input()
print('NO' if string.lower().find('хорош') == -1  else'YES')
