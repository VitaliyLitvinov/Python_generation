day = int(input())
weight = float(input())
parpose = 100 - day*0.2
print('Все идет по плану' if weight <= parpose else 'Что-то пошло не так')
print(f'#{day} ДЕНЬ: ТЕКУЩИЙ ВЕС = {weight} кг, ЦЕЛЬ по ВЕСУ = {parpose} кг')