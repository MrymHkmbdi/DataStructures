import unittest
from queue import Queue


class TestQueue(unittest.TestCase):
    def test_is_empty(self):
        queue_ = Queue()
        self.assertEqual(queue_.size, 0)

    def test_add_to_queue(self):
        queue_ = Queue()
        queue_.add_to_queue(1)
        queue_.add_to_queue(2)
        queue_.add_to_queue(3)
        queue_.add_to_queue(4)
        self.assertEqual(queue_.front.data, 1)
        self.assertEqual(queue_.rear.data, 4)

    def test_delete_from_queue(self):
        queue_ = Queue()
        queue_.add_to_queue(1)
        queue_.add_to_queue(2)
        queue_.add_to_queue(3)
        queue_.add_to_queue(4)
        queue_.delete_from_queue()
        self.assertEqual(queue_.front.data, 2)


if __name__ == '__main__':
    unittest.main()
