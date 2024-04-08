class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity # capacity variable
        self.cache = {} # cache memory to save data
        self.left, self.right = Node(0,0), Node(0,0) # dummy nodes to operate data b/w

        # connecting dummy nodes
        self.left.next, self.right.prev = self.right, self.left

    # Helper Functions
    def remove(self, node):
        prv, nxt = node.prev, node.next
        prv.next, nxt.prev = nxt, prv
        
        
    def insert(self, node):
        node.prev = self.right.prev
        node.next = self.right

        self.right.prev.next = node
        self.right.prev = node
    # end

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])    # remove from the list 
            self.insert(self.cache[key])    # add to the right because of recent access

            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        # if the key is already present
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
            
        # insert at the right, because of recent access
        self.insert(self.cache[key])
        
        # if the cache mem is full
        if len(self.cache) > self.capacity:
            temp = self.left.next
            self.remove(temp)
            del self.cache[temp.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
