import pytest
from src.Circle import Circle
from src.Triangle import Triangle
def test_circle1():
    circle = Circle("Сircle", 10)
    assert circle.area == 314.1592653589793

def test_circle2():
    circle = Circle("Сircle", 10)
    assert circle.perimetr == 62.83185307179586

def test_circle3():
    circle = Circle("Сircle", 0)
    assert circle.perimetr == 62.83185307179586
    with pytest.raises(ValueError):
        ValueError("cant create a Square")

def test_add_area():
    circle_1 = Circle("Сircle", 10)
    triangle_1 = Triangle("name1", 13, 14, 15)
    result = circle_1.add_area(triangle_1)
    assert result == 398.1592653589793

def test_add_area1():
    circle_1 = Circle("Сircle", 10)
    foo_examle = 0
    with pytest.raises(ValueError):
        circle_1.add_area(foo_examle)