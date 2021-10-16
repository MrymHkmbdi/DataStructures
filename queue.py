class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:

    def __init__(self):
        self.front = self.rear = None
        self.size = 0

    def is_empty(self):
        return self.front is None

    def add_to_queue(self, data):
        new_node = Node(data)
        print('inserting...{}'.format(data))
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def delete_from_queue(self):

        if self.is_empty():
            return
        new_node = self.front
        print('removing...{}'.format(new_node.data))
        self.front = new_node.next

        if self.front is None:
            self.rear = None

    def queue_size(self):
        return self.size
