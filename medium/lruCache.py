class LRUCache(object):
    
    class Node(object):
        def __init__(self, key, value, prev=None, next=None):
            self.key = key
            self.value = value
            self.prev = prev
            self.next = next

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}
        self.head = self.Node(0, 0)
        self.tail = self.Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.addToHead(node)
            return node.value
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key not in self.cache:
            node = self.Node(key, value)
            self.cache[key] = node
            self.addToHead(node)
            if len(self.cache) > self.capacity:
                remove_node = self.tail.prev
                self.remove(remove_node)
                del self.cache[remove_node.key]
        else:
            node = self.cache[key]
            node.value = value
            self.remove(node)
            self.addToHead(node)
        
    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
        
    def addToHead(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)