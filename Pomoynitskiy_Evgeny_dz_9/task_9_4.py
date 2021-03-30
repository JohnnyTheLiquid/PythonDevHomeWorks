class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} go-go.')

    def stop(self):
        print(f'{self.name} stops.')

    def turn(self, direction):
        print(f'{self.name} turns {direction}')

    def show_speed(self):
        print(f'{self.name} speed is {self.speed} mph')

class SportCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police=False)


class TownCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police=False)

    def show_speed(self):
        if not self.speed > 60:
            print(f"{self.name} speed is {self.speed} mph. It's ok")
        else:
            print(f'{self.name} is breaking speed limit for {self.speed - 60} mph! Warning!')

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police=False)

    def show_speed(self):
        if not self.speed > 40:
            print(f"{self.name} speed is {self.speed} mph. It's ok")
        else:
            print(f'{self.name} is breaking speed limit for {self.speed - 60} mph! Warning!')

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police=True)

auto_0 = PoliceCar(120, 'blue', 'Ford')
auto_0.go()
auto_0.stop()
auto_0.turn('left')
auto_0.show_speed()
print(auto_0.color)

auto_1 = TownCar(90, 'black', 'Mazda')
auto_1.go()
auto_1.stop()
auto_1.turn('left')
auto_1.show_speed()
print(auto_1.color)

auto_2 = WorkCar(75, 'white', 'Doodge')
auto_2.go()
auto_2.stop()
auto_2.turn('left')
auto_2.show_speed()
print(auto_2.color)
