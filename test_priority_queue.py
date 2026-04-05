import unittest
from Lab4_2 import PriorityQueue

class TestPriorityQueue(unittest.TestCase):
    def setUp(self):
        self.pq = PriorityQueue()
        self.pq.insert("Task A", 3)
        self.pq.insert("Task B", 5)
        self.pq.insert("Task C", 1)

    def test_peek(self):
        self.assertEqual(self.pq.peek().value, "Task B")

    def test_extract_max(self):
        max_node = self.pq.extract_max()
        self.assertEqual(max_node.value, "Task B")

    def test_insert(self):
        self.pq.insert("Task D", 10)
        self.assertEqual(self.pq.peek().value, "Task D")

if __name__ == "__main__":
    unittest.main()