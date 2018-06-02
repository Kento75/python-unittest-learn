import unittest
from calc.calc import Calculator


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.calc = Calculator()
        print("create calculator")

    def test_add(self):
        self.assertEqual(self.calc.add(5, 2), 7)

    def test_sub(self):
        self.assertEqual(self.calc.sub(5, 2), 3)

    def test_mul(self):
        self.assertEqual(self.calc.mul(5, 2), 10)

    def test_div(self):
        self.assertEqual(self.calc.div(5, 2), 2)


if __name__ == "__main__":
    unittest.main()
