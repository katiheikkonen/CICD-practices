import unittest
import src.calculator as laskin

class TestCalculator(unittest.TestCase):
    def test_int_numbers_plus(self):
        result = laskin.plus(2, 3)
        self.assertEqual(result, 5)

    def test_negative_int_numbers_plus(self):
        result = laskin.plus(-2, -3)
        self.assertEqual(result, -5)

    def test_if_returns_floats_plus(self):
        result = laskin.plus(2.4, 3.2)
        self.assertEqual(result, 5.6)

    def test_if_returns_integer_and_float_plus(self):
        result = laskin.plus(2, 3.2)
        self.assertEqual(result, 5.2)

    def test_error_if_not_numbers_plus(self):
        with self.assertRaises(TypeError):
            laskin.plus(1, "a")

if __name__ == '__main__':
    unittest.main()
