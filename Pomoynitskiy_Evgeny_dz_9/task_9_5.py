class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def __init__(self):
        super().__init__(self)

    def draw(self):
        print('Drawing with a pen')


class Pencil(Stationery):
    def __init__(self):
        super().__init__(self)

    def draw(self):
        print('Drawing with a pencil')


class Handle(Stationery):
    def __init__(self):
        super().__init__(self)

    def draw(self):
        print('Drawing with a handle')

pen = Pen()
pen.draw()

pencil = Pencil()
pencil.draw()

handle = Handle()
handle.draw()
