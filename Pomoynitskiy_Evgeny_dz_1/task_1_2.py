# инициализаруем пустой список
sq_list = []

# наполняем кубами нечетных чисел
i = 0
while i <= 1000:
    if i % 2 == 1:
        sq_list.append(pow(i, 3))
    i += 1

# введем переменную для искомой суммы
sum_seven = 0
# проитерируем по массиву, проверяя условие делимости суммы разрядов на 7.
for element in sq_list:
    a = 1
    b = 10 # можно было бы обойтись и одной переменнной, но с двумя нагляднее
    expression = 0
    # сумму разрядов получим с помощью цикла
    while a <= element:
        expression += element % b // a
        a = 10 * a
        b = 10 * a
    # если сумма разрядов делится на 7 без остатка, прибавляем элемент массива к сумме
    if expression % 7 == 0:
        sum_seven += element
        # да, проверка через вывод - дурной тон, но зато наглядно
        #print(element, sum_seven)

print('Сумма элементов, делящихся на 7 : ', sum_seven)

# изменяем массив, прибавляя к каждому элементу 17
for idx, l in enumerate(sq_list):
    sq_list[idx] = l + 17

# применим цикл, который уже использовали ранее, к обновленному массиву
sum_seven_2 = 0
for element in sq_list:
    a = 1
    b = 10
    expression = 0
    while a <= element:
        expression += element % b // a
        a = 10 * a
        b = 10 * a
    if expression % 7 == 0:
        sum_seven_2 += element

print('Сумма элементов, делящихся на 7 в обновленном массиве : ', sum_seven_2)
