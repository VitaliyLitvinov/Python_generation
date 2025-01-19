# На вход программе подаётся строка текста,
# содержащая различные натуральные числа.
# Вам необходимо переставить максимальный и минимальный элементы местами
# и вывести изменённую строку
s = input().split()
s_min = min(s, key=int)
s_max = max(s, key=int)
i_min = s.index(s_min)
i_max = s.index(s_max)
s[i_max] = s_min
s[i_min] = s_max
print(*s, sep=' ')
# OR
list_str = input().split()
string = [int(item) for item in list_str]

ind_min, ind_max = string.index(min(string)), string.index(max(string))
string[ind_min], string[ind_max] = string[ind_max], string[ind_min]

print(*string)
