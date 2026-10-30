
class BinaryHeap:
    def __init__(self):
        self.data = []

        def push(self, item):
            self.data.append(item)
            self.sift_up(len(self.data) - 1)
        def pop(self):
            if not self.data:
                raise IndexError("heap is empty")

            if len(self.data) == 1:
                return self._ata.pop()

            top = self.data[0]
            self.data[0] = self.data.pop()
            self._sift_down(0)
            return top
        def peek(self):
            if not self.data:
                raise IndexError("heap is empty")
            return self.data[0]

        def replace_top(self, item):
            if not self.data:
                raise IndexError("heap is empty")

            old_top = self.data[0]
            self.data[0] = item
            self.sift_down(0)
            return old_top
        def __len__(self):
            return len(self.data)