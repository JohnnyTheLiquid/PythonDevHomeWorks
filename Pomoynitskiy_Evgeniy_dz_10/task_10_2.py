from abc import ABC, abstractmethod

class Clothes(ABC):
    @abstractmethod
    def cloth_spend(self):
        pass

class Overcoat(Clothes):
    def __init__(self, v):
        self.v = v

    @property
    def cloth_spend(self):
        return self.v / 6.5 + 0.5

class Suite(Clothes):
    def __init__(self, h):
        self.h = h

    @property
    def cloth_spend(self):
        return 2 * self.h + 0.3

a = Overcoat(5)
print(a.cloth_spend)
b = Suite(3)
print(b.cloth_spend)
