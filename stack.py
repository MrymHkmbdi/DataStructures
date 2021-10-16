class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.stackSize = 0

    def push(self, data):
        temp = Node(data)
        if self.top is None:
            self.top = temp
            self.stackSize = self.stackSize + 1
        else:
            temp.next = self.top
            self.top = temp
            self.stackSize = self.stackSize + 1

    def pop(self):
        if self.top is None:
                print('Stack is Empty')
                return
        else:
                temp = self.top
                self.top = self.top.next
                tempdata = temp.data
                self.stackSize = self.stackSize - 1
                del temp
                return tempdata

    def top_element(self):
        if self.top is None:
            print('Stack is Empty')
            return
        else:
            return self.top.data
