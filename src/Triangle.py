import math

from src.Figure import Figure


class Triangle(Figure):
    def __init__(self, name, a, b, c):
        self.name = "Triangle"
        self.a = a
        self.b = b
        self.c = c
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("cant create a Triangle")

    @property
    def area(self) -> float:
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    @property
    def perimetr(self) -> float:
        return self.a + self.b + self.c

