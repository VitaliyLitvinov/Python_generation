a = str(input())
b = str(input())
if a == 'красный':
    if b == 'красный':
        print('красный')
    elif b == 'синий':
        print('фиолетовый')
    elif b == 'желтый':
        print('оранжевый')
    else:
        print('ошибка цвета')
elif a == 'синий':
    if b == 'синий':
        print('синий')
    elif b == 'желтый':
        print('зеленый')
    elif b == 'красный':
        print('фиолетовый')
    else:
        print('ошибка цвета')
elif a == 'желтый':
    if b == 'красный':
        print('оранжевый')
    elif b == 'синий':
        print("зеленый")
    elif b == 'желтый':
        print('желтый')
    else:
        print('ошибка цвета')
else:
    print('ошибка цвета')