# инициализируем переменные - неизменяемую часть слова и массив с окончаниями
word_root = 'процент'
word_ends = ['', 'а', 'ов']
# запрашваем пользователя и преобразуем ответ в целое число
lever = int(input('Введите целое число процентов от 1 до 20'))

# в зависимости от числа, прибавляем то или иное окончание
if lever == 1:
    print(lever, word_root + word_ends[0])
elif 1 < lever < 5:
    print(lever, word_root + word_ends[1])
elif 5 <= lever <= 20:
    print(lever, word_root + word_ends[2])