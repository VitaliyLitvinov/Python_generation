from random import *
x = randint(1, 100)
print("Добро пожаловать в числовую угадайку")

def is_valid(number: str):
    return 1 <= int(number) <= 100
cnt = 0
while True:
    print("Введите число: ", end='')
    number = int(input())
    cnt += 1
    if not is_valid(number):
        print("А может быть все-таки введем целое число от 1 до 100?")
        continue
    else:
        if number == x:
            print('Вы угадали, поздравляем!')
            break
        elif number > x:
            print('Ваше число больше загаданного, попробуйте еще разок')
        elif number < x:
            print('Ваше число меньше загаданного, попробуйте еще разок')
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
print(f'Число ваших попыток: {cnt}')