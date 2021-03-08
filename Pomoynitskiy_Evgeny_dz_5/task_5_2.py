def odd_to_n_(n):
    """решение без yield"""
    return [i for i in range(1, n + 1, 2) if i % 2 != 0]

# по факту мы создали список в результате работы функции

res = [i for i in odd_to_n_(15)]
print(res)
