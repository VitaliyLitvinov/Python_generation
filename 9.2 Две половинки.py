# На вход программе подаётся строка текста. Напишите программу,
# которая разрежет её на две равные части, переставит их местами и выведет на экран.

from math import floor
string = input()
slice = (len(string) + 1) // 2
print(string[slice:],string[:slice], sep='')