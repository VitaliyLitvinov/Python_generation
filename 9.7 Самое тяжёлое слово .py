# Под "тяжестью" слова будем понимать сумму кодов по таблице Unicode
# всех символов этого слова. Напишите программу, которая принимает
# 4 слова и находит среди них самое тяжёлое слово. Если самых тяжёлых
# слов будет несколько, то программа должна вывести первое из них.

heaviest = ''
sum_word = 0
heavy_word = 0

for i in range(4):
    word = input()
    for i in range(0,len(word)):
        sum_word += int(ord(word[i]))
    if sum_word > heavy_word:
        heavy_word = sum_word
        heaviest = word
    sum_word = 0
print(heaviest)
