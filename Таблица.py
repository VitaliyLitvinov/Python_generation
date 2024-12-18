num = int(input())
tmp = 1
while tmp != num + 1:
    for i in range(5):
        print(tmp, end=' ')
    tmp += 1
    print()