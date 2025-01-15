# На вход программе подаётся натуральное число n(n≥2). Затем поступают
# n целых чисел. Напишите программу, которая создаёт из указанных чисел список,
# состоящий из сумм текущего и предыдущего чисел
n = int(input())
list_num = []
previos = 0
for i in range(n):
    num = int(input())
    list_num.append(num + previos)
    previos = num
print(list_num[1:])

