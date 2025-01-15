# На вход программе подаются натуральное число n и n строк, а затем число
# k. Напишите программу, которая выводит k-ую букву из введённых строк
# на одной строке без пробелов.
n = int(input())
words = []
for i in range(n):
    word = input()
    words.append(word)
k = int(input())
k_words = ''
for i in words:
    if len(i) >= k:
        k_words += i[k-1]
print(k_words)