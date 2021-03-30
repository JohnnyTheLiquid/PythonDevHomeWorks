class Matrix:
    def __init__(self, m):
        self.m = m

    def __str__(self):
        matr = ''
        for i in self.m:
            row = [str(j) for j in i]
            row = '\t'.join(row)
            matr += row + '\n' * 2
        return matr

    def __add__(self, other):
        matr_1 = self.m
        matr_2 = other.m
        if len(matr_1) != len(matr_2):
            return 'Matrices have different dimension!'
        else:
            from itertools import zip_longest
            summ = [[val_1 + val_2 for val_1, val_2 in zip_longest(row_1, row_2, fillvalue=0)] for row_1, row_2 in zip(matr_1, matr_2)]
            return Matrix(summ)


m = [[1, 2, 3], [3, 4, 5]]
n = [[9, 8, 7], [7, 6, 5]]
l = [[1, 2], [3, 4]]
o = [[1, 2], [3, 4], [5, 6]]

matr_1 = Matrix(m)
matr_2 = Matrix(n)
matr_3 = Matrix(l)
matr_4 = Matrix(o)

print(matr_1)
print(matr_1 + matr_2)
print(matr_1 + matr_3)
print(matr_1 + matr_4)
