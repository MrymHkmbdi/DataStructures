class MaxHeap:
    def __init__(self):
        self.heap = []
        self.front = 1

    def get_parent(self, i):
        return int((i-1)/2)

    def get_left_child(self, i):
        return 2*i+1

    def get_right_child(self, i):
        return 2*i+2

    def has_parent(self, i):
        return self.get_parent(i) < len(self.heap)

    def has_left_child(self, i):
        return self.get_left_child(i) < len(self.heap)

    def has_right_child(self, i):
        return self.get_right_child(i) < len(self.heap)

    def insert(self, key):
        self.heap.append(key)
        self.heapify(len(self.heap) - 1)

    def get_max(self):
        return self.heap[0]

    def heapify(self, i):
        while self.has_parent(i) and self.heap[i] > self.heap[self.get_parent(i)]:
            self.heap[i], self.heap[self.get_parent(i)] = self.heap[self.get_parent(i)], self.heap[i]
            i = self.get_parent(i)

    def delete_max(self):
        popped = self.heap[0]
        self.heap.remove(self.heap[0])
        self.heapify(self.heap[0])
        return popped

    def print_heap(self):
        print(self.heap)


if __name__ == "__main__":
    print('The minHeap is ')
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
    ans = max_heap.delete_max()
    max_heap.print_heap()
    print('max value is {}'.format(max_heap.heap[0]))
