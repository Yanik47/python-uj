import pytest
from point import Point
from rectangle import Rectangle

@pytest.fixture
def setup_rectangles():
    return {
        "A": Rectangle(0, 0, 5, 2),
        "B": Rectangle(-2, -2.4, 0.3, 6.1),
        "C": Rectangle.from_points((Point(0, 0), Point(5, 2))),
    }

def test_exception():
    with pytest.raises(ValueError, match="wrong values"):
        Rectangle(1, 1, 0, 0)

def test_str(setup_rectangles):
    A, B = setup_rectangles["A"], setup_rectangles["B"]
    assert str(A) == "[(0, 0), (5, 2)]"
    assert str(B) == "[(-2, -2.4), (0.3, 6.1)]"

def test_repr(setup_rectangles):
    A, B = setup_rectangles["A"], setup_rectangles["B"]
    assert repr(A) == "Rectangle(0, 0, 5, 2)"
    assert repr(B) == "Rectangle(-2, -2.4, 0.3, 6.1)"

def test_equal(setup_rectangles):
    A, B = setup_rectangles["A"], setup_rectangles["B"]
    assert A == A
    assert A != B

def test_center(setup_rectangles):
    A, B = setup_rectangles["A"], setup_rectangles["B"]
    assert A.center == Point(2.5, 1)
    assert B.center == Point(-0.85, 1.85)

def test_area(setup_rectangles):
    A, B = setup_rectangles["A"], setup_rectangles["B"]
    assert A.area() == 10
    assert B.area() == 19.55

def test_move(setup_rectangles):
    A, B = setup_rectangles["A"], setup_rectangles["B"]
    assert A.move(4, 2) == Rectangle(4, 2, 9, 4)
    assert B.move(0, -1.5) == Rectangle(-2, -3.9, 0.3, 4.6)

def test_intersection(setup_rectangles):
    A, B = setup_rectangles["A"], setup_rectangles["B"]
    assert A.intersection(B) == Rectangle(0, 0, 0.3, 2)
    with pytest.raises(ValueError, match="overlap is not a rectangle"):
        A.intersection(Rectangle(10, 10, 11, 11))

def test_cover(setup_rectangles):
    A, B = setup_rectangles["A"], setup_rectangles["B"]
    assert A.cover(B) == Rectangle(-2, -2.4, 5, 6.1)

def test_make4(setup_rectangles):
    A = setup_rectangles["A"]
    assert A.make4() == [
        Rectangle(0, 0, 2.5, 1.0),
        Rectangle(2.5, 0, 5, 1.0),
        Rectangle(0, 1.0, 2.5, 2),
        Rectangle(2.5, 1.0, 5, 2),
    ]

def test_from_points(setup_rectangles):
    C = setup_rectangles["C"]
    assert C == Rectangle(0, 0, 5, 2)
    with pytest.raises(ValueError, match="Input must be a list or tuple of two points"):
        Rectangle.from_points((Point(1, 1),))

def test_left_right_top_bottom(setup_rectangles):
    A, B = setup_rectangles["A"], setup_rectangles["B"]
    assert A.left == 0
    assert A.right == 5
    assert A.top == 2
    assert A.bottom == 0

    assert B.left == -2
    assert B.right == 0.3
    assert B.top == 6.1
    assert B.bottom == -2.4

def test_height_width(setup_rectangles):
    A, B = setup_rectangles["A"], setup_rectangles["B"]
    assert A.height == 2
    assert A.width == 5
    assert B.height == 8.5
    assert B.width == 2.3

def test_corners(setup_rectangles):
    A, B = setup_rectangles["A"], setup_rectangles["B"]

    assert A.top_left == Point(0, 2)
    assert A.top_right == Point(5, 2)
    assert A.bottom_left == Point(0, 0)
    assert A.bottom_right == Point(5, 0)

    assert B.top_left == Point(-2, 6.1)
    assert B.top_right == Point(0.3, 6.1)
    assert B.bottom_left == Point(-2, -2.4)
    assert B.bottom_right == Point(0.3, -2.4)
