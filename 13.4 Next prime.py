def is_prime(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    return True if count == 2 else False


def get_next_prime(num):
    num += 1
    while not is_prime(num):
        num += 1

    return num


n = int(input())
print(get_next_prime(n))