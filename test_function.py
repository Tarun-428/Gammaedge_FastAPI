import unittest
from function import add, subtract

class TestAddFunction(unittest.TestCase):
    def test_add_positive_number(self):
        result = add(1,2)
        self.assertEqual(result,3)
    def test_add_negative_number(self):
        result = add(-1,-1)
        self.assertEqual(result,-2)
    def test_add_zero(self):
        result = add(0,5)
        self.assertEqual(result,5)

if __name__ == '__main__':
    unittest.main()