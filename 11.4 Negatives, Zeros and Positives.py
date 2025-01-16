# На вход программе подаются натуральное число n, а затем
# n целых чисел. Напишите программу, которая сначала выводит
# все отрицательные числа, затем нули, а затем все положительные числа,
# каждое на отдельной строке. Числа должны быть выведены в том же порядке,
# в котором они были введены.
list_neg = []
list_zer = []
list_pos = []
for _ in range(int(input())):
    num = int(input())
    if num < 0:
        list_neg.append(num)
    elif num == 0:
        list_zer.append(num)
    else:
        list_pos.append(num)
print(*list_neg, sep='\n')
print(*list_zer, sep='\n')
print(*list_pos, sep='\n')
