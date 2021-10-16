import unittest
from heap import MaxHeap


class TestHeap(unittest.TestCase):
    def test_insert(self):
        max_heap = MaxHeap()
        max_heap.insert(5)
        max_heap.insert(3)
        max_heap.insert(17)
        max_heap.insert(10)
        max_heap.insert(84)
        max_heap.insert(19)
        max_heap.insert(6)
        max_heap.insert(22)
        max_heap.insert(9)
        max_heap.delete_max()
        max_heap.print_heap()
        self.assertEqual(max_heap.heap[4], 5)

    def test_delete_max(self):
        max_heap = MaxHeap()
        max_heap.insert(5)
        max_heap.insert(3)
        max_heap.insert(17)
        max_heap.insert(10)
        max_heap.insert(84)
        max_heap.insert(19)
        max_heap.insert(6)
        max_heap.insert(22)
        max_heap.insert(9)
        max_heap.delete_max()
        max_heap.print_heap()
        self.assertEqual(max_heap.heap[0], 22)



