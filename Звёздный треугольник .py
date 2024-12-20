num = int(input())
tmp = 1
while tmp < int(num / 2) + 1:
    for i in range(1, int(num / 2) + 2):
        print('*' * i)
        tmp += 1
    for i in range(int(num / 2), 0, -1):
        print('*' * i)
    print()
