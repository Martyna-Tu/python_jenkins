import unittest
import main


class Tests(unittest.TestCase):
    def test_method_to_add_numbers(self):
        self.assertEqual(10, main.add(5,5))

    def test_method_to_subtract_numbers(self):
        self.assertEqual(2, main.subtract(7,5))

    def test_method_to_multiply_numbers(self):
        self.assertEqual(100, main.multiply(25,4))

    def test_method_to_divide_numbers(self):
        self.assertEqual(4, main.divide(20,5))


if __name__ == "__main__":
    unittest.main()