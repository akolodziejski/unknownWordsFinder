import unittest
__author__ = 'Areo'


class MyTest(unittest.TestCase):
    def test_even(self):
        for x in range(6):
            with self.subTest(x=x):
                print()
                self.assertEqual(x % 2, 0)
