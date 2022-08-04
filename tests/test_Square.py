import pytest
from src.Square import Square
from src.Triangle import Triangle
def test_square1():
    square = Square("Square", 10, 10)
    assert square.area == 100

def test_square2():
    square = Square("Square", 10, 10)
    assert square.perimetr == 40



def test_square3():
    square = Square("Square", 10, 20)
    assert square.perimetr == 40
    with pytest.raises(ValueError):
        ValueError("cant create a Square")



def test_add_area():
    square_1 = Square("Square", 10, 10)
    triangle_1 = Triangle("name1", 13, 14, 15)
    result = square_1.add_area(triangle_1)
    assert result == 184

def test_add_area1():
    square_1 = Square("Square", 10, 10)
    foo_examle = 0
    with pytest.raises(ValueError):
        square_1.add_area(foo_examle)