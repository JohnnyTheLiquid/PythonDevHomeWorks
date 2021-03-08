def odd_to_n(n):
    """решение через yield"""
    for i in range(1, n + 1, 2):
        yield i

res = [i for i in odd_to_n(15)]
print(res)
