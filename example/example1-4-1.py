import unittest


class MyTestCase(unittest.TestCase):
    def setUp(self):
        print('setup')

    def tearDown(self):
        print('teardown')

    def test_test1(self):
        print('test1')

    def test_test2(self):
        print('test2')


if __name__ == '__main__':
    unittest.main()

