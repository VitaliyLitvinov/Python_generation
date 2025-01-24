
def print_digit_sum(num):
    sum_n = sum(int(i) for i in str(n))
    print(sum_n)

n = int(input())

print_digit_sum(n)