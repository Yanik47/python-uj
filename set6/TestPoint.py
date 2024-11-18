from point import Point
import unittest
from math import sqrt as Msqrt

class TestPoint(unittest.TestCase):
    def setUp(self):
        self.zero = Point(0, 0)

    def testStr(self):
        self.assertEqual(str(Point(3, 5)), "(3, 5)")
        self.assertEqual(str(Point(4.2, 7.16)), "(4.2, 7.16)")

    def testRepr(self):
        self.assertEqual(repr(Point(3, 5)), "Point(3, 5)")
        self.assertEqual(repr(Point(4.2, 7.16)), "Point(4.2, 7.16)")

    def testEqual(self):
        self.assertEqual(Point(3, 5) == Point(3, 5), True)
        self.assertEqual(Point(4.2, 7.16) == Point(-3, 15), False)

    def testNotEqual(self):
        self.assertEqual(Point(3, 5) != Point(3, 5), False)
        self.assertEqual(Point(4.2, 7.16) != Point(-3, 15), True)

    def testAdd(self):
        self.assertEqual(Point(4, 0.16) + Point(-3, 15), Point(1, 15.16))
        self.assertEqual(Point(4, 5) + Point(0, 1), Point(4, 6))
    
    def testSub(self):
        self.assertEqual(Point(4, 0.16) - Point(-3, 15), Point(7, -14.84))
        self.assertEqual(Point(4, 5) - Point(0, 1), Point(4, 4))

    def testMul(self):
        self.assertEqual(Point(4, 5) * Point(2, 4.5), 30.5)
        self.assertEqual(Point(10, 0) * Point(2, 7), 20)

    def testCross(self):
        self.assertEqual(Point(4, 5).cross(Point(2, 4.5)), 8)
        self.assertEqual(Point(10, 0).cross(Point(2, 7)), 70)
    
    def testLength(self):
        self.assertEqual(Point(3, 4).length(), 5)
        self.assertEqual(Point(4, 7).length(), Msqrt(65))

    def testHash(self):
        self.assertEqual(hash(Point(3, 4.2)), hash((3, 4.2)))

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()