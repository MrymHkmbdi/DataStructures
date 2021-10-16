import unittest
from stack import Stack


class TestStack(unittest.TestCase):
    def test_push(self):
        new_stack = Stack()
        new_stack.push(1)
        new_stack.push(2)
        new_stack.push(3)
        new_stack.push(4)
        self.assertEqual(new_stack.top.data, 4)

    def test_pop(self):
        new_stack = Stack()
        new_stack.push(1)
        new_stack.push(2)
        new_stack.push(3)
        new_stack.push(4)
        new_stack.pop()
        self.assertEqual(new_stack.top.data, 3)
        self.assertEqual(new_stack.stackSize, 3)


if __name__ == '__main__':
    unittest.main()
