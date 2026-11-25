
class BinaryHeap:
    def __init__(self, max_heap=False):
        self.data = []
        self.max_heap = max_heap

    def push(self, item):
        self.data.append(item)
        self._sift_up(len(self.data) - 1)

    def _is_less(self, a, b):
        if self.max_heap:
            return a > b
        return a < b

    def _parent(self, i):
        return (i - 1) // 2

    def _left(self, i):
        return 2 * i + 1

    def _right(self, i):
        return 2 * i + 2

    def _swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def _sift_up(self, i):
        while i > 0:
            p = self._parent(i)
            if self._is_less(self.data[i], self.data[p]):
                self._swap(i, p)
                i = p
            else:
                break

    def _sift_down(self, i):
        n = len(self.data)
        while True:
            best = i
            left = self._left(i)
            right = self._right(i)

            if left < n and self._is_less(self.data[left], self.data[best]):
                best = left
            if right < n and self._is_less(self.data[right], self.data[best]):
                best = right

            if best == i:
                break
            self._swap(i, best)
            i = best

    def pop(self):
        if not self.data:
            raise IndexError("heap is empty")

        if len(self.data) == 1:
            return self.data.pop()

        top = self.data[0]
        self.data[0] = self.data.pop()
        self._sift_down(0)
        return top

    def heapify(self, items):
        self.data = list(items)
        for i in range(len(self.data) // 2 - 1, -1, -1):
            self._sift_down(i)
            
    def peek(self):
        if not self.data:
            raise IndexError("heap is empty")
        return self.data[0]

    def size(self):
        return len(self.data)

    def replace_top(self, item):
        if not self.data:
            raise IndexError("heap is empty")

        old_top = self.data[0]
        self.data[0] = item
        self._sift_down(0)
        return old_top

    def is_empty(self):
        return len(self.data) == 0