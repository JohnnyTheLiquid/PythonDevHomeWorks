from decimal import Decimal

# создаем список цен
prices = [57.08, 46.51, 97, 66.5, 77.15, 88, 99, 21.21, 36]

# выводим цены, форматируя
for p in prices:
    a = str(Decimal(p).quantize(Decimal('1.00'))).split('.')
    a[1] = a[1].zfill(2)
    a.insert(1, 'руб')
    a.append('коп')
    print(" ".join(a), end=', ')


print('\n',"ID объекта до сортировки ", id(prices))
# Произведем сортировку встроенным методом
prices.sort()
print('\n', "ID объекта после сортировки {} \n и сам отсортированный список {}".format(id(prices), prices))

# Поскольку список уже отсортирован по возарстанию, достаточно его развернуть через слайс
new_prices = prices[::-1]
print('\n', "ID объекта после разворота в обратном порядке {} \n и сам отсортированный список {}".format(id(new_prices),new_prices))

# цены 5-ти самых дорогих товаров - это 5 первых элементов. Минимум кода - через слайс
print ("\n Цены 5-ти самых дорогих товаров {}, \n они же отсортированы по возрастанию {}".format(new_prices[:5],
                                                                                                 new_prices[4::-1]))
