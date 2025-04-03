# Program 1

class MinHeap:
    def __init__(self):
        self.heap = []
        self.size = 0

    def get_left_child(self, index):
        left_index = 2 * index + 1
        if left_index < self.size:
            return self.heap[left_index]
        return None

    def get_right_child(self, index):
        right_index = 2 * index + 2
        if right_index < self.size:
            return self.heap[right_index]
        return None

    def get_parent(self, index):
        if index == 0:
            return None
        parent_index = (index - 1) // 2
        return self.heap[parent_index]

    def swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def remove_root(self):
        if self.size == 0:
            return None
        root_value = self.heap[0]
        self.heap[0] = self.heap[self.size - 1]
        self.heap.pop()
        self.size -= 1
        self.sink_down(0)
        return root_value

    def sink_down(self, index):
        smallest = index
        left_child = 2 * index + 1
        right_child = 2 * index + 2

        if left_child < self.size and self.heap[left_child] < self.heap[smallest]:
            smallest = left_child

        if right_child < self.size and self.heap[right_child] < self.heap[smallest]:
            smallest = right_child

        if smallest != index:
            self.swap(index, smallest)
            self.sink_down(smallest)

    def insert(self, value):
        self.heap.append(value)
        self.size += 1
        self.bubble_up(self.size - 1)

    def bubble_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] < self.heap[parent_index]:
                self.swap(index, parent_index)
                index = parent_index
            else:
                break

    def __str__(self):
        return str(self.heap)


def main():
    minheap = MinHeap()


    minheap.insert(99)
    minheap.insert(72)
    minheap.insert(61)
    minheap.insert(58)

    print("Heap after initial insertions:", " ".join(map(str, minheap.heap)))

    minheap.insert(100)
    print("After inserting 100:", " ".join(map(str, minheap.heap)))

    minheap.insert(75)
    print("After inserting 75:", " ".join(map(str, minheap.heap)))

    minheap.remove_root()
    print("After removing root:", " ".join(map(str, minheap.heap)))

    minheap.remove_root()
    print("After removing root:", " ".join(map(str, minheap.heap)))


if __name__ == "__main__":
    main()
