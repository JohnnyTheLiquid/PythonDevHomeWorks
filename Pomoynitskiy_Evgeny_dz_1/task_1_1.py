duration = int(input('Введите длительность промежутка в секундах'))

if duration <=60:
    print('Это эквивалентно', duration, 'сек')
elif 60 < duration <= 3600:
    print('Это эквивалентно', duration // 60, 'мин', duration % 60, 'сек')
elif 3600 < duration <= 86400:
    print('Это эквивалентно', duration // 3600, 'часов', (duration % 3600) // 60, 'мин', (duration % 3600) % 60, 'сек')
