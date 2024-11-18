from point import Point
from math import sqrt as Msqrt

class Rectangle:

    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):  # konstuktor
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
        self.pt3 = Point(x3, y3)
        self.pt4 = Point(x4, y4)
        self.points = {self.pt1, self.pt2, self.pt3, self.pt4}

    def __str__(self):
        return "[" + str(self.pt1) + ", " + str(self.pt2) + ", " + str(self.pt3) +", "+ str(self.pt4)+"]"

    def __repr__(self):
        return "Rectangle(" + str(self.pt1.x) + ", " + str(self.pt1.y) + ", " + str(self.pt2.x) + ", " + str(self.pt2.y) + ", " + str(self.pt3.x) + ", " + str(self.pt3.y) +  ", " + str(self.pt4.x) + ", " + str(self.pt4.y) + ")"

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.points == other.points
        return False
        

    def __ne__(self, other):
        return not self == other

    def center(self):
        Sx = sum(pt.x for pt in self.points) / 4
        Sy = sum(pt.y for pt in self.points) / 4
        return Point(Sx, Sy)

    def area(self):
        x_min = min(p.x for p in self.points)
        x_max = max(p.x for p in self.points)
        y_min = min(p.y for p in self.points)
        y_max = max(p.y for p in self.points)
        
        width = x_max - x_min
        height = y_max - y_min
        return width * height

    def move(self, x, y):
        return Rectangle(
            self.pt1.x + x, self.pt1.y + y,
            self.pt2.x + x, self.pt2.y + y,
            self.pt3.x + x, self.pt3.y + y,
            self.pt4.x + x, self.pt4.y + y
        )