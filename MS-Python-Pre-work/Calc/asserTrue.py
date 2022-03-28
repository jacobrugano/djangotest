import unittest
from calculator import Calculator

class TestString(unittest.TestCase):
    def test_addTwoNumbers(self):
        result = Calculator.addTwoNumbers(1,2)
        self.assertEqual(result,3)

    def test_substractTwoNumbers(self):
        result = Calculator.substractTwoNumbers (5,2)
        self.assertEqual(result,3)

    def test_multiplyTwoNumbers (self):
        result = Calculator.multiplyTwoNumbers(3,8)
        self.assertEqual(result, 24)

    def test_divideTwoNumbers (self):
        result = Calculator.divideTwoNumbers(10,2)
        self.assertEqual(result, 5)



if __name__ == '__main__':
    unittest.main()