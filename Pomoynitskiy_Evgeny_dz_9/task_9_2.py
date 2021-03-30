class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def volume_asph(self):
        return f'{self._width * self._length * 25 * 5 / 1000} tonns'

r_1 = Road(20, 200)
r_2 = Road(15, 100)
print(r_1.volume_asph(), sep='\n')
print(r_2.volume_asph(), sep='\n')
print(f'attributes: {r_1._length} and {r_1._width}')
