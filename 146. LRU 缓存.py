class Node:
    def __init__(self, key=None, value=None, pre=None, nxt=None):
        self.key = key
        self.value = value
        self.pre = pre
        self.next = nxt

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {}
        self.idx = 0
        self.init_link_list()

    def get(self, key: int) -> int:
        if key in self.dic:
            self.move_to_tail(self.dic[key])
            return self.dic[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.dic[key].value = value
            self.move_to_tail(self.dic[key])
        else:
            if self.capacity == 0:
                remove_key = self.remove_head()
                del self.dic[remove_key]
            else:
                self.capacity -= 1

            node = Node(key, value)
            self.insert_tail(node)
            self.dic[key] = node

    def init_link_list(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.pre = self.head

    def insert_tail(self, node):
        node.pre = self.tail.pre
        node.next = self.tail
        self.tail.pre.next = node
        self.tail.pre = node

    def remove_head(self):
        node = self.head.next
        self.head.next = self.head.next.next
        self.head.next.pre = self.head
        key = node.key
        del node
        return key

    def move_to_tail(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre
        self.insert_tail(node)