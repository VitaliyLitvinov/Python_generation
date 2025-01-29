def is_password_good(password):
    flag = True
    if (len(password) >= 8 and
            password != password.lower() and
            password != password.upper() and
            any(ch.isdigit() for ch in password)):
        flag = True
    else:
        flag = False
    return flag

txt = input()

print(is_password_good(txt))