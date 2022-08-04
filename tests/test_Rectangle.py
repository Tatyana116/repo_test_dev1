import pytest
from src.Rectangle import Rectangle
from src.Triangle import Triangle
def test_rectangle1():
    rectangle = Rectangle("Rectangle", 10, 11)
    assert rectangle.area == 110

def test_rectangle2():
    rectangle = Rectangle("Rectangle", 10, 11)
    assert rectangle.perimetr == 40

def test_rectangle3():
    rectangle = Rectangle("Rectangle", 10, 20)
    assert rectangle.perimetr == 40
    with pytest.raises(ValueError):
        ValueError("cant create a Rectangle")

def test_add_area():
    rectangle_1 = Rectangle("Rectangle", 10, 11)
    triangle_1 = Triangle("name1", 13, 14, 15)
    result = rectangle_1.add_area(triangle_1)
    assert result == 194

def test_add_area1():
    rectangle_1 = Rectangle("Rectangle", 10, 11)
    foo_examle = 0
    with pytest.raises(ValueError):
        rectangle_1.add_area(foo_examle)