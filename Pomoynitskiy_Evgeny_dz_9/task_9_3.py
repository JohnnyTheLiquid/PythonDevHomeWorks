class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return (self._income['wage'] * 12) * (1 + self._income['bonus'])

work_1 = Position('Ivan', 'Petrov', 'staff', 100, 0.50)

print(work_1.get_full_name())
print(work_1.get_total_income())
print(work_1._income)
