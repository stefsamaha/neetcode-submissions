class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        # left side = least recently used
        # right side = most recently used
        self.left = Node(0, 0)
        self.right = Node(0, 0)

        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        before = node.prev
        after = node.next

        before.next = after
        after.prev = before

    def add_to_end(self, node):
        last = self.right.prev

        last.next = node
        node.prev = last

        node.next = self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]

        # Since it was just accessed, it becomes most recently used
        self.remove(node)
        self.add_to_end(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value

            # A put also counts as using the key
            self.remove(node)
            self.add_to_end(node)
        else:
            node = Node(key, value)
            self.cache[key] = node
            self.add_to_end(node)

        # Remove the least recently used item if over capacity
        if len(self.cache) > self.capacity:
            least_recent = self.left.next

            self.remove(least_recent)
            del self.cache[least_recent.key]