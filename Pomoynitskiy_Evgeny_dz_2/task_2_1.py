expr = [15 * 3,
15 / 3,
15 // 2,
15 ** 2]

for idx, e in enumerate(expr, start=1):
    print("Результат выражения {} имеет тип {}".format(idx, type(e)))
