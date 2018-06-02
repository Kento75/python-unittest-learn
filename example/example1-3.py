import unittest


class MyTestCase(unittest.TestCase):
    def test_equal(self):
        result = 1 + 2
        self.assertEqual(result, 3)

    def test_not_equal(self):
        result = 1 + 2
        self.assertNotEqual(result, 10)

    def test_match_string(self):
        string = "Hello" + "World"
        self.assertEqual(string, "HelloWorld")

    def test_start_match_string(self):
        string = "HelloWorld"
        self.assertTrue(string.startswith('H'))

    def test_exist_string(self):
        string = "HelloWorld"
        self.assertIn('oWo', string)


if __name__ == '__main__':
    unittest.main()

