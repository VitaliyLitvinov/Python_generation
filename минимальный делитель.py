
num = int(input())
divider = 2
while num % divider != 0:
    divider += 1

print(divider)

# OR

num = int(input())
divider = 2
while True:
    if num % divider == 0:
        break
    divider += 1

print(divider)