class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def print_list(self):
        head = self.head
        while head is not None:
            print(head.data)
            head = head.next

    def insert_begin(self, new_data):
        the_node = Node(new_data)
        the_node.next = self.head
        self.head = the_node

    def insert_end(self, new_data):
        NewNode = Node(new_data)
        if self.head is None:
            self.head = NewNode
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = NewNode

    def insert_between(self, middle_node, new_data):
        if middle_node is None:
            print("The mentioned node is absent")
            return

        NewNode = Node(new_data)
        NewNode.next = middle_node.next
        middle_node.next = NewNode

    def remove_node(self, key):
        head = self.head

        if head is not None:
            if head.data == key:
                self.head = head.next
                head = None
                return
        while head is not None:
            if head.data == key:
                break
            prev = head
            head = head.next

        if head is None:
            return

        prev.next = head.next
        head = None

    def list_size(self):
        return self.size

    def last_node(self):
        head = self.head
        while head is not None:
            if head.next is None:
                return head.data


if __name__ == "__main__":
    new_list = LinkedList()
    new_list.insert_begin(1)
    new_list.insert_begin(2)
    new_list.insert_begin(3)
    new_list.insert_between(new_list.head.next, 5)
    new_list.insert_end(4)
    new_list.print_list()
