class Cell:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        return self.n + other.n

    def __sub__(self, other):
        if self.n - other.n > 0:
            return self.n - other.n
        else:
            return 'Error! Result should be positive. Substract smaller from bigger'

    def __mul__(self, other):
        return self.n * other.n

    def __floordiv__(self, other):
        return self.n // other.n

    def make_order(self, m):
        rows = self.n // m
        last_row = self.n % m
        return (("*" * m + '\n') * rows, "*" * last_row)

a = Cell(16)
b = Cell(3)

print(a + b,'\t', a - b, '\t', b - a, '\n', a * b, '\n', a // b, '\n', b // a )

print(a.make_order(3))
