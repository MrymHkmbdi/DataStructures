import unittest
from linkedlist import LinkedList


class TestLinkedList(unittest.TestCase):
    def test_remove(self):
        new_list = LinkedList()
        new_list.insert_begin(1)
        new_list.insert_begin(2)
        new_list.insert_begin(3)
        new_list.remove_node(2)

        self.assertEqual(new_list.head.data, 3, 'expected 3 but got {}'.format(new_list.head.data))
        self.assertEqual(new_list.head.next.data, 1, 'expected 1 but got {}'.format(new_list.head.next.data))

    def test_insert_between(self):
        new_list = LinkedList()
        new_list.insert_begin(1)
        new_list.insert_begin(2)
        new_list.insert_begin(3)
        new_list.remove_node(2)
        new_list.insert_between(new_list.head.next, 5)

        self.assertEqual(new_list.head.next.next.data, 5)

    def test_insert_begin(self):
        new_list = LinkedList()
        new_list.insert_begin(1)
        new_list.insert_begin(2)
        new_list.insert_begin(3)

        self.assertEqual(new_list.head.data, 3)

    def test_insert_end(self):
        new_list = LinkedList()
        new_list.insert_begin(1)
        new_list.insert_begin(2)
        new_list.insert_begin(3)
        new_list.insert_end(4)

        self.assertEqual(new_list.last_node(), 4)


if __name__ == '__main__':
    unittest.main()
