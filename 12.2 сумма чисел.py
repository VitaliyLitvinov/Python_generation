l = [int(i) for i in input().split()]
sum_l = sum(l)
print(*l, sep='+', end='')
print(f'={sum_l}')
