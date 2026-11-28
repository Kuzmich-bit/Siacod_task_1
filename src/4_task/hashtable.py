class Node:
    __slots__ = ("key", "value", "next")

    def __init__(self, key, value, nxt=None):
        self.key, self.value, self.next = key, value, nxt


class HashTable:
    MAX_LOAD = 0.75

    def __init__(self, hash_func, eq_func, capacity=8):
        self.hash = hash_func
        self.eq = eq_func
        self.buckets = [None] * capacity
        self.size = 0

    def __len__(self):
        return self.size

    def _index(self, key, cap=None):
        return self.hash(key) % (cap or len(self.buckets))

    def find(self, key):
        node = self.buckets[self._index(key)]
        while node is not None:
            if self.eq(node.key, key):
                return node.value
            node = node.next
        return None

    def put(self, key, value):
        i = self._index(key)
        node = self.buckets[i]
        while node is not None:
            if self.eq(node.key, key):
                node.value = value          # замена
                return False
            node = node.next
        self.buckets[i] = Node(key, value, self.buckets[i])  # вставка в голову
        self.size += 1
        if self.size / len(self.buckets) > self.MAX_LOAD:
            self._resize(len(self.buckets) * 2)
        return True

    def remove(self, key):
        i = self._index(key)
        prev, node = None, self.buckets[i]
        while node is not None:
            if self.eq(node.key, key):
                if prev is None:
                    self.buckets[i] = node.next
                else:
                    prev.next = node.next
                self.size -= 1
                return True
            prev, node = node, node.next
        return False

    def items(self):
        for node in self.buckets:
            while node is not None:
                yield node.key, node.value
                node = node.next

    def _resize(self, new_cap):
        old = self.buckets
        self.buckets = [None] * new_cap
        for node in old:
            while node is not None:
                nxt = node.next
                j = self._index(node.key, new_cap)
                node.next = self.buckets[j]
                self.buckets[j] = node
                node = nxt
        print(f"[таблица] расширение: ёмкость {len(old)} -> {new_cap}")


def string_hash(s):
    h = 0
    for ch in s:
        h = (h * 31 + ord(ch)) & 0xFFFFFFFF
    return h


def string_eq(a, b):
    return a == b