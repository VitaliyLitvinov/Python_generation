# На вход программе подаются натуральное число n, затем
# строк, затем число k – количество поисковых запросов, затем
# k строк – поисковые запросы. Напишите программу, которая выводит
# все введённые строки, в которых встречаются одновременно все поисковые запросы.

n = int(input())
list_n = []
for i in range(n):
    list_n.append(input())
n_search = int(input())
list_search = []
for i in range(n_search):
    list_search.append(input())
for i in list_n:
    flag = True
    for k in list_search:
        if k.lower() not in i.lower():
            flag = False
    if flag == True:
        print(i)