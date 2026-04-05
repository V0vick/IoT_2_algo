import unittest
from lab5_2 import compute_max_experience

class TestCareer(unittest.TestCase):
    def test_example1(self):
        L = 4
        pyramid = [
            [4],
            [3, 1],
            [2, 1, 5],
            [1, 3, 2, 1]
        ]
        self.assertEqual(compute_max_experience(L, pyramid), 12)

    def test_example2(self):
        L = 1
        pyramid = [[9999]]
        self.assertEqual(compute_max_experience(L, pyramid), 9999)

    def test_example3(self):
        L = 5
        pyramid = [
            [0],
            [1, 1],
            [0, 0, 0],
            [1, 1, 1, 1],
            [0, 1, 0, 1, 0]
        ]
        self.assertEqual(compute_max_experience(L, pyramid), 3)

    def test_single_zero(self):
        L = 1
        pyramid = [[0]]
        self.assertEqual(compute_max_experience(L, pyramid), 0)

    def test_increasing_triangle(self):
        L = 3
        pyramid = [
            [1],
            [2, 3],
            [4, 5, 6]
        ]
        self.assertEqual(compute_max_experience(L, pyramid), 10)


if __name__ == "__main__":
    unittest.main()