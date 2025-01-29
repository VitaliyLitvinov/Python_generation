def is_correct_bracket(text):
    balance = 0
    for i in text:
        if i == '(':
            balance += 1
        else:
            balance -= 1
        if balance < 0:
            return False
    return True if balance == 0 else False


# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))