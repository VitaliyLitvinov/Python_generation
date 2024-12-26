number = int(input())
bin_num = ''
while number != 0:
    if number % 2 == 0:
        bin_num += '0'
        number /= 2
    if number % 2 != 0:
        bin_num += '1'
        number = int(number / 2)

for i in bin_num[::-1]:
    print(i, end='')
