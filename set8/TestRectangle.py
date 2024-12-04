from point import Point
from rectangle import Rectangle
import unittest

class TestReactangle(unittest.TestCase):
    def setUp(self):
        self.A = Rectangle(0, 0, 5, 2)
        self.B = Rectangle(-2, -2.4, 0.3, 6.1)

    def testException(self):
        try:
            C = Rectangle(1, 1, 0, 0)
        except ValueError as exct:
            self.assertEqual(exct.args[0], "wrong values")

    def testStr(self):
        self.assertEqual(str(self.A), "[(0, 0), (5, 2)]")
        self.assertEqual(str(self.B), "[(-2, -2.4), (0.3, 6.1)]")

    def testRepr(self):
        self.assertEqual(repr(self.A), "Rectangle(0, 0, 5, 2)")
        self.assertEqual(repr(self.B), "Rectangle(-2, -2.4, 0.3, 6.1)")

    def testEqual(self):
        self.assertEqual(self.A == self.A, True)
        self.assertEqual(self.A == self.B, False)

    def testNotEqual(self):
        self.assertEqual(self.A != self.A, False)
        self.assertEqual(self.A != self.B, True)
    
    def testCenter(self):
        self.assertEqual(self.A.center(), Point(2.5, 1))
        self.assertEqual(self.B.center(), Point(-0.85, 1.85))

    def testArea(self):
        self.assertEqual(self.A.area(), 10)
        self.assertEqual(self.B.area(), 19.55)

    def testMove(self):
        self.assertEqual(self.A.move(4, 2), Rectangle(4, 2, 9, 4))
        self.assertEqual(self.B.move(0, -1.5), Rectangle(-2, -3.9, 0.3, 4.6))
    
    def testIntersection(self):
        self.assertEqual(self.A.intersection(self.B), Rectangle(0, 0, 0.3, 2))
        try:
            self.A.intersection(Rectangle(10, 10, 11, 11))
        except ValueError as exct:
            self.assertEqual(exct.args[0], "overlap is not a rectangle")

    def testCover(self):
        self.assertEqual(self.A.cover(self.B), Rectangle(-2, -2.4, 5, 6.1))

    def testMake4(self):
        self.assertEqual(self.A.make4(),
        [Rectangle(0, 0, 2.5, 1.0),
         Rectangle(2.5, 0, 5, 1.0),
         Rectangle(0, 1.0, 2.5, 2),
         Rectangle(2.5, 1.0, 5, 2),
        ])

    def setUp(self):
        self.A = Rectangle(0, 0, 5, 2)
        self.B = Rectangle(-2, -2.4, 0.3, 6.1)
        self.C = Rectangle.from_points((Point(0, 0), Point(5, 2)))

    def testCenter(self):
        self.assertEqual(self.A.center, Point(2.5, 1))
        self.assertEqual(self.B.center, Point(-0.85, 1.85))

    def testFromPoints(self):
        self.assertEqual(self.C, Rectangle(0, 0, 5, 2))
        try:
            Rectangle.from_points((Point(1, 1),))
        except ValueError as exct:
            self.assertEqual(exct.args[0], "Input must be a list or tuple of two points")

    def testLeftRightTopBottom(self):
        self.assertEqual(self.A.left, 0)
        self.assertEqual(self.A.right, 5)
        self.assertEqual(self.A.top, 2)
        self.assertEqual(self.A.bottom, 0)
        self.assertEqual(self.B.left, -2)
        self.assertEqual(self.B.right, 0.3)
        self.assertEqual(self.B.top, 6.1)
        self.assertEqual(self.B.bottom, -2.4)

    def testHeightWidth(self):
        self.assertEqual(self.A.height, 2)
        self.assertEqual(self.A.width, 5)
        self.assertEqual(self.B.height, 8.5)
        self.assertEqual(self.B.width, 2.3)

    def testCorners(self):
        self.assertEqual(self.A.top_left, Point(0, 2))
        self.assertEqual(self.A.top_right, Point(5, 2))
        self.assertEqual(self.A.bottom_left, Point(0, 0))
        self.assertEqual(self.A.bottom_right, Point(5, 0))

        self.assertEqual(self.B.top_left, Point(-2, 6.1))
        self.assertEqual(self.B.top_right, Point(0.3, 6.1))
        self.assertEqual(self.B.bottom_left, Point(-2, -2.4))
        self.assertEqual(self.B.bottom_right, Point(0.3, -2.4))


    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()