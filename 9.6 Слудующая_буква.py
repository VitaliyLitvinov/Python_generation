letter = input()
print(chr(ord(letter) + 1) if ord(letter) != 1071 else 'Дальше букв нет')