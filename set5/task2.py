import fracs as Fr
import unittest

class TestFractions(unittest.TestCase):
    def setUp(self):
        self.zero_fraction = [0, 1]

    def test_fraction_addition(self):
        self.assertEqual(Fr.fraction_addition([3, 4], [2, 5]), [23, 20])
        self.assertEqual(Fr.fraction_addition([-9, 7], [5, 14]), [-13, 14])

    def test_fraction_subtraction(self): 
        self.assertEqual(Fr.fraction_subtraction([7, 8], [3, 8]), [1, 2])
        self.assertEqual(Fr.fraction_subtraction([15, 45], [-5, 9]), [8, 9])

    def test_fraction_multiplication(self):
        self.assertEqual(Fr.fraction_multiplication([-3, 7], [2, -5]), [6, 35])
        self.assertEqual(Fr.fraction_multiplication([9, 4], [7, 3]), [21, 4])

    def test_fraction_division(self):
        self.assertEqual(Fr.fraction_division([5, 6], [2, 3]), [5, 4])
        self.assertEqual(Fr.fraction_division([-8, 9], [3, -2]), [16, 27])

    def test_is_fraction_positive(self):
        self.assertEqual(Fr.is_fraction_positive([-2, 3]), False)
        self.assertEqual(Fr.is_fraction_positive([0, 1]), True)
        self.assertEqual(Fr.is_fraction_positive([5, -7]), False)
        self.assertEqual(Fr.is_fraction_positive([8, 3]), True)

    def test_is_fraction_zero(self):
        self.assertEqual(Fr.is_fraction_zero([4, 9]), False)
        self.assertEqual(Fr.is_fraction_zero([0, 8]), True)
        self.assertEqual(Fr.is_fraction_zero([0, -10]), True)

    def test_compare_fractions(self):
        self.assertEqual(Fr.compare_fractions([2, 5], [4, 10]), 0)
        self.assertEqual(Fr.compare_fractions([-3, 8], [6, -16]), 0)
        self.assertEqual(Fr.compare_fractions([7, 10], [2, 3]), 1)
        self.assertEqual(Fr.compare_fractions([-11, 13], [5, 9]), -1)

    def test_fraction_to_float(self):
        self.assertEqual(Fr.fraction_to_float([3, 8]), 0.375)
        self.assertEqual(Fr.fraction_to_float([-7, 9]), -0.7777777777777778)
        self.assertEqual(Fr.fraction_to_float([2, 7]), 0.2857142857142857)

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()
