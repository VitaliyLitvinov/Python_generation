
a = int(input())
b = int(input())
cnt = 0
for i in range(a, b + 1):
    for k in range(2, i + 1):
        if i % k == 0:
            cnt += 1
    if cnt == 1:
        print(i)
    cnt = 0