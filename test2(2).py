from lab2_2_2 import num_sum

import unittest

class Testnumsum(unittest.TestCase):
    def test_exampletrue(self):
        self.assertTrue(num_sum([1, 2, 3], 6))

    def test_examplefalse(self):
        self.assertFalse(num_sum([1, 2, 4], 10))

    def test_exampleBignumbers(self):
        self.assertTrue(num_sum([10**9, 2, 3, 5], 10**9 + 2 + 5))

    def test_examplefalse(self):
        self.assertFalse(num_sum([1, 1, 1], 3))
        self.assertFalse(num_sum([1, 1, 2], 10))

if __name__ == "__main__":
    unittest.main()
