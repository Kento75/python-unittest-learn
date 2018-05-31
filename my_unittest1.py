import unittest

from my_func import add, sub


class MyTestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)

    def test_sub(self):
        self.assertEqual(sub(3, 1), 2)


if __name__ == '__main__':
    unittest.main()
