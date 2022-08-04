import math

from src.Figure import Figure

class Circle (Figure):
    def __init__(self, name, R):
        self.name = "Circle"
        self.R = R

        if R == 0:
            raise ValueError('cant create a Circle')

    @property
    def area(self):
        return math.pi * self.R ** 2

    @property
    def perimetr(self):
        perimetr = 2 * math.pi * self.R
        return perimetr