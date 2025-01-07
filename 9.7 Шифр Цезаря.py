n = int(input())
string = input()
new_string = ''
for i in string:
    if (ord(i) - n) < 97:
        new_string += chr(ord(i) - n + 26)
    else:
        new_string += chr(ord(i) - n)
print(new_string)