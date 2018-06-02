import unittest
from calc.calc import Calculator
from parameterized import parameterized


class MyTestCase(unittest.TestCase):

    @parameterized.expand([
        (5, 2, 7),
        (6, 2, 8),
        (7, 2, 9),
    ])
    def test_add(self, input_a, input_b, expected_result):
        print("test_add()")
        print("input_a:", input_a)
        print("input_b:", input_b)
        print("expected_result:", expected_result)

        calc = Calculator()
        self.assertEqual(calc.add(input_a, input_b), expected_result)


if __name__ == "__main__":
    unittest.main()
