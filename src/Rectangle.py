from src.Figure import Figure

class Rectangle (Figure):
    def __init__(self,name, a, b ):
        self.name = "Rectangle"
        self.a = a
        self.b = b
        if a == b:
            raise ValueError('cant create a Rectangle')

    @property
    def area(self):
        area = self.a * self.b
        return area

    @property
    def perimetr(self):
        perimetr = self.a * 4
        return perimetr