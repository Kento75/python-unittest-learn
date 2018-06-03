import unittest
from calc.calc import Calculator


class MyTestCase(unittest.TestCase):
    def test_div(self):
        with self.assertRaises(ZeroDivisionError):
            calc = Calculator()
            calc.div(5, 0)


if __name__ == "__main__":
    unittest.main()

