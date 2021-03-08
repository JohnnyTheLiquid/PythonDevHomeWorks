src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [23, 1, 3, 10, 4, 11]

from time import perf_counter

# решение короткое по записи, но долгое. Для маленького списка это не заметно, но для больших д.б. видно
start = perf_counter()

res = [el for el in src if src.count(el) == 1]
print (perf_counter() - start)
print(res)

# решение альтернативное
start = perf_counter()

unique_val = set()
temp = set()
for el in src:
    if el not in temp:
        unique_val.add(el)
    else:
        unique_val.discard(el)
    temp.add(el)

unique_val_ord = [el for el in src if el in unique_val]

print (perf_counter() - start)
print(unique_val_ord)
