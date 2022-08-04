import pytest
from src.Triangle import Triangle
from src.Square import Square
def test_triangle1():
    triangle = Triangle("Triangle", 13, 14, 15)
    assert triangle.area == 84


def test_triangle2():
    triangle = Triangle("Triangle", 13, 14, 15)
    assert triangle.perimetr == 42

def test_add_area():
    triangle_1 = Triangle("name1", 13, 14, 15)
    square_1 = Square(14, 14)
    result = triangle_1.add_area(square_1)
    assert result == 280

def test_triangle3():
    triangle_2 = Triangle("Triangle", 1, 2, 20)
    square_2 = Square(14, 14)
    with pytest.raises(ValueError):
        triangle_2.add_area(square_2)

def test_add_area1():
    triangle_1 = Triangle("name1", 13, 14, 15)
    foo_examle = 0
    with pytest.raises(ValueError):
        triangle_1.add_area(foo_examle)

