# На вход программе подаётся строка. Напишите программу,
# которая подсчитывает количество буквенных символов в нижнем регистре.

string = input()
counter = 0
list_number = ('1','2','3','4','5','6','7','8','9','0')
for i in range(0,len(string)):
    if string[i] == string[i].lower() and string[i] not in list_number:
        counter += 1
print(counter)