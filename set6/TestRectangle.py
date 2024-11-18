from point import Point
from rectangle import Rectangle
import unittest

class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.A = Rectangle(0, 0, 4, 0, 4, 3, 0, 3)
        self.B = Rectangle(-2, -2, 3, -2, 3, 4, -2, 4)
        self.C = Rectangle(0, 0, 4, 0, 4, 3, 0, 3)

    def testStr(self):
        self.assertEqual(str(self.A), "[(0, 0), (4, 0), (4, 3), (0, 3)]")
        self.assertEqual(str(self.B), "[(-2, -2), (3, -2), (3, 4), (-2, 4)]")

    def testRepr(self):
        self.assertEqual(repr(self.A), "Rectangle(0, 0, 4, 0, 4, 3, 0, 3)")
        self.assertEqual(repr(self.B), "Rectangle(-2, -2, 3, -2, 3, 4, -2, 4)")

    def testEqual(self):
        self.assertEqual(self.A == self.A, True)
        self.assertEqual(self.A == self.C, True)
        self.assertEqual(self.A == self.B, False)

    def testNotEqual(self):
        self.assertEqual(self.A != self.A, False)
        self.assertEqual(self.A != self.B, True)

    def testCenter(self):
        self.assertEqual(self.A.center(), Point(2, 1.5))
        self.assertEqual(self.B.center(), Point(0.5, 1))

    def testArea(self):
        self.assertEqual(self.A.area(), 12)
        self.assertEqual(self.B.area(), 30)

    def testMove(self):
        newRect = self.A.move(1, 1)
        expected = Rectangle(1, 1, 5, 1, 5, 4, 1, 4)
        self.assertEqual(newRect, expected)
        self.assertEqual(newRect.center(), Point(3, 2.5))
        self.assertEqual(newRect.area(), 12)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
