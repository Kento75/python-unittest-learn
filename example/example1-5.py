import unittest


class MyTestCase(unittest.TestCase):
    def test_test1(self):
        print("test1")

    @unittest.skip("not implemented yet")
    def test_test2(self):
        print("test2")

    def test_test3(self):
        print("test3")


if __name__ == "__main__":
    unittest.main()

