n = int(input())
n1 = 0
n2 = 1
for i in range(1, n+1):
    n = n1 + n2
    print(n, end=' ')
    n1 = n
    n2 = n - n2