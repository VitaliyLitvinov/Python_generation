num = int(input())
tmp = 1
while tmp < num + 1:
    for i in range(1,10):
        print(f'{tmp} + {i} = {tmp + i}')
    tmp += 1
    print()