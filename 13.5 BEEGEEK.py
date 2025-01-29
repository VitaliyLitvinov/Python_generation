def is_valid_password(password):
    password = password.split(':')
    a, b, c = password[0], int(password[1]), int(password[2])
    if len(password) != 3 or a != a[::-1] or c % 2 != 0:
        return False
    for i in range(2, b):
        if b % i == 0:
            return False
    return True


psw = input()
print(is_valid_password(psw))