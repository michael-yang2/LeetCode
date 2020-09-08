class Node():
    def __init__(self,key = None, val = None):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
        
class LRUCache:
    def add_to_end(self, node):
        previous_last = self.tail.prev
        previous_last.next = node
        node.prev = previous_last
        node.next = self.tail
        self.tail.prev = node
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    def __init__(self, capacity: int):
        self.dict = {} #dict of key:Node
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.length = 0
    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        corresponding_node = self.dict[key]
        self.remove(corresponding_node)
        self.add_to_end(corresponding_node)
        return corresponding_node.val
    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            curr_node = self.dict[key]
            curr_node.val = value
            self.remove(curr_node)
            self.add_to_end(curr_node)
        else:
            if self.capacity == self.length:
                k = self.head.next.key
                self.remove(self.head.next)
                del self.dict[k]
                self.length-=1
            self.length+=1
            new_node = Node(key,value)
            self.dict[key] = new_node
            self.add_to_end(new_node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)