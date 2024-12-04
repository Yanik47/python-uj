from point import Point
from math import sqrt as Msqrt

class Rectangle:

    def __init__(self, x1, y1, x2, y2):
        if not x1 < x2 or not y1 < y2:
            raise ValueError("wrong values")
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):
        return "[" + str(self.pt1) + ", " + str(self.pt2) +"]"

    def __repr__(self):
        return "Rectangle(" + str(self.pt1.x) + ", " + str(self.pt1.y) + ", " + str(self.pt2.x) + ", " + str(self.pt2.y) +")"

    def __eq__(self, other):
        return self.pt1 == other.pt1 and self.pt2 == other.pt2
        
    def __ne__(self, other):
        return not self == other

    @property
    def center(self):
        Sx = round((self.pt1.x + self.pt2.x) / 2, 8)
        Sy = round((self.pt1.y + self.pt2.y) / 2, 8)
        return Point(Sx, Sy)

    def area(self):
        width = self.pt2.x - self.pt1.x
        height = self.pt2.y - self.pt1.y
        return round((width * height), 2)


    def move(self, x, y):
        return Rectangle(
            self.pt1.x + x, self.pt1.y + y,
            self.pt2.x + x, self.pt2.y + y
        )

    def intersection(self, other):
        if self.pt2.x <= other.pt1.x or self.pt2.y <= other.pt1.y or self.pt1.x >= other.pt2.x or self.pt1.y >= other.pt2.y:
            raise ValueError("overlap is not a rectangle")
        x1 = max(self.pt1.x, other.pt1.x)
        y1 = max(self.pt1.y, other.pt1.y)
        x2 = min(self.pt2.x, other.pt2.x)
        y2 = min(self.pt2.y, other.pt2.y)
        if x1 < x2 and y1 < y2:
            return Rectangle(x1, y1, x2, y2)
        else:
            return None
        
    def cover(self, other):
        x1 = min(self.pt1.x, other.pt1.x)
        y1 = min(self.pt1.y, other.pt1.y)
        x2 = max(self.pt2.x, other.pt2.x)
        y2 = max(self.pt2.y, other.pt2.y)
        return Rectangle(x1, y1, x2, y2)    
    
    def make4(self):
        center = self.center
        return [
            Rectangle(self.pt1.x, self.pt1.y, center.x, center.y),
            Rectangle(center.x, self.pt1.y, self.pt2.x, center.y),
            Rectangle(self.pt1.x, center.y, center.x, self.pt2.y),
            Rectangle(center.x, center.y, self.pt2.x, self.pt2.y)
        ]
    @classmethod
    def from_points(cls, points):
        if not isinstance(points, (list, tuple)) or len(points) != 2:
            raise ValueError("Input must be a list or tuple of two points")
        p1, p2 = points
        return cls(p1.x, p1.y, p2.x, p2.y)
        
    @property
    def left(self):
        return min(self.pt1.x, self.pt2.x)
    
    @property
    def right(self):
        return max(self.pt1.x, self.pt2.x)
    
    @property
    def top(self):
        return max(self.pt1.y, self.pt2.y)
    
    @property
    def bottom(self):
        return min(self.pt1.y, self.pt2.y)
    
    @property
    def height(self):
        return abs(self.top - self.bottom)  

    @property
    def width(self):
        return abs(self.right - self.left)

    @property
    def top_left(self):
        return Point(self.left, self.top)

    @property
    def top_right(self):
        return Point(self.right, self.top)

    @property
    def bottom_left(self):
        return Point(self.left, self.bottom)
    
    @property
    def bottom_right(self):
        return Point(self.right, self.bottom)  
