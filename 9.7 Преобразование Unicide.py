# На вход программе подаётся строка текста.
# Расшифруйте текст, заменив все конструкции [u-<номер символа в таблице Unicode>]
# на соответствующие буквы русского алфавита, и выведите его.


string = input()
for i in range(64):
    letter = int(ord('А')) + i
    if str(letter) in string:
        string = string.replace(f'[u-{letter}]', chr(letter))
print(string)