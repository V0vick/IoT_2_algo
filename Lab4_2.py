import subprocess
import sys

class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def _parent(self, index):
        return (index - 1) // 2

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _heapify_up(self, index):
        while index > 0:
            parent = self._parent(index)
            if self.heap[index].priority > self.heap[parent].priority:
                self._swap(index, parent)
                index = parent
            else:
                break

    def _heapify_down(self, index):
        size = len(self.heap)
        while True:
            left = self._left_child(index)
            right = self._right_child(index)
            largest = index

            if left < size and self.heap[left].priority > self.heap[largest].priority:
                largest = left
            if right < size and self.heap[right].priority > self.heap[largest].priority:
                largest = right

            if largest != index:
                self._swap(index, largest)
                index = largest
            else:
                break

    def insert(self, value, priority):
        node = Node(value, priority)
        self.heap.append(node)
        self._heapify_up(len(self.heap) - 1)

    def extract_max(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def peek(self):
        return self.heap[0] if self.heap else None

    def __repr__(self):
        return f"PriorityQueue({self.heap})"


if __name__ == "__main__":
    print("Запускаємо юнітест")

    test_file = "Lab4.2(2)/test_priority_queue.py"

    proc = subprocess.run([sys.executable, test_file], capture_output=True, text=True)

    print("Return code:", proc.returncode)
    if proc.stdout:
        print(proc.stdout)
    if proc.stderr:
        print(proc.stderr)