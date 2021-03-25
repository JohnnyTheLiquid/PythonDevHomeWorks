class TrafficLight:
    def __init__(self, color='red'):
        self.color = color

    def running(self):
        from time import sleep
        from colorama import Fore
        for t, c, col in [(7, Fore.RED, 'red'), (2, Fore.YELLOW, 'yellow'), (5, Fore.GREEN, 'green')]:
            print(c + f'Light turns to {col}')
            sleep(t)

traff_light = TrafficLight()
traff_light.running()
