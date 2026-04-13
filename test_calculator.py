import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(multiply(2,3), 6)
        self.assertEqual(multiply(-4,5),-20)
        self.assertEqual(multiply(0, 10), 0)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(10, 2), 5)
        self.assertEqual(div(20, 10), 2)
        self.assertEqual(div(5, 2), 2.5)
    # ##########################
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        # call log function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     logarithm(0, 5)
        with self.assertRaises(ValueError):
            logarithm(0, 5)


    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(5, 12), 13)



    def test_sqrt(self): # 3 assertions
        # Test for invalid argument, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #    square_root(NUM)
        # Test basic function
        with self.assertRaises(ValueError):
            square_root(-4)

        self.assertEqual(square_root(25), 5)

class TestCalculator(unittest.TestCase):
    def test_add(self):  # 3 assertions
        assert add(1, 2) == 3
        assert add(2, 3) == 5
        assert add(3, 4) == 7

    def test_subtract(self):  # 3 assertions
        assert sub(1, 2) == -1
        assert sub(10, 5) == 5
        assert sub(-1, -2) == 1

    ######## Partner 2
    def test_divide_by_zero(self):  # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self):  # 3 assertions
        assert logarithm(1, 2) == 0
        assert logarithm(7, 49) == 0.5
        assert logarithm(8, 2) == 3

    def test_log_invalid_base(self):  # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(5, 0)

# Do not touch this
if __name__ == "__main__":
    unittest.main()