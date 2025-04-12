class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.oldest = Node(0, 0)
        self.latest = Node(0, 0)
        self.oldest.next = self.latest
        self.latest.prev = self.oldest

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        self.remove(self.cache[key])
        self.insert(self.cache[key])
        return self.cache[key].val

    def remove(self, node: Node) -> None:
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def insert(self, node: Node) -> None:
        prev = self.latest.prev
        next = self.latest
        node.prev = prev
        prev.next = node
        next.prev = node
        node.next = next

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.oldest.next
            self.remove(lru)
            del self.cache[lru.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
