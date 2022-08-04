from src.Figure import Figure

class Square(Figure):
    def __init__(self, name, a, b ):
        self.name = "Square"
        self.a = a
        self.b = b
        if a != b:
            raise ValueError('cant create a Square')
    @property
    def area(self):
        area = self.a * self.b
        return area

    @property
    def perimetr(self):
        perimetr = self.a * 4
        return perimetr