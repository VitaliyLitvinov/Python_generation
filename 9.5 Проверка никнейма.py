nicname = input()
flag = False
if (4 < len(nicname) < 16
    and nicname[1:len(nicname) + 1].isdigit()
    and nicname[0] == '@'):
    print('Correct')
elif (4 < len(nicname) < 16
    and nicname[1:len(nicname) + 1].isalnum()
    and nicname[1:len(nicname) + 1].islower()
    and nicname[0] == '@'):
    print('Correct')
else:
    print('Incorrect')