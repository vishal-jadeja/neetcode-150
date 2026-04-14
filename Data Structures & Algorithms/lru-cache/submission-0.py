class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next = self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.head = self.tail = Node(0, 0)
        self.head.next, self.tail.prev = self.tail, self.head

    def remove(self, node: Node):
        prevNode, nextNode = node.prev, node.next
        prevNode.next, nextNode.prev = nextNode, prevNode

    def insert(self, node: Node):
        prevNode = self.tail.prev
        node.prev, node.next = prevNode, self.tail
        prevNode.next = node
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove(self.cache[key])
            self.insert(self.cache[key])
        else:
            if self.cap == len(self.cache):
                currNode, nextNode = self.head.next, self.head.next.next
                self.head.next = nextNode
                nextNode.prev = self.head
                del self.cache[currNode.key]
            node = Node(key, value)
            self.insert(node)
            self.cache[key] = node