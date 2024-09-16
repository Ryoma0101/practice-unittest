import unittest
from main import *


class TestHello(unittest.TestCase):
    def test_main(self):
        self.assertEqual(hello(), "Hello, World!追加")


class TestNumpy(unittest.TestCase):
    def test_example_function(self):
        self.assertEqual(example_function(), 3.0)


if __name__ == '__main__':
    unittest.main()
