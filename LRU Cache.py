class LRUCache:
    class ListNode:
        def __init__(self, key, value):
            self.val = value
            self.key = key
            self.pre = None
            self.next = None
    # @param capacity, an integer
    def __init__(self, capacity):
        # write your code here
        self.capacity = capacity
        self.count = 0
        self.root = self.ListNode(-1, -1)
        self.tail = self.ListNode(-1, -1)
        self.root.next = self.tail
        self.tail.pre = self.root
        self.dicts = {}

    # @return an integer
    def get(self, key):
        #ListNode write your code here
        if key in self.dicts:
            ## delete from root
            node = self.dicts[key]
            self.root.next = node.next
            self.root.next.pre = self.root
            ## insert the tail
            node.next = self.tail
            self.tail.pre.next = node
            node.pre = self.tail.pre
            self.tail.pre = node
            print node.val
            return node.val
        else:
            print -1
            return -1
        
    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        print key, value
        # write your code here
        if self.count >= self.capacity:
            self.get(self.root.next.key)
            self.dicts.pop(self.tail.pre.key)
            self.tail.pre.key = key
            self.tail.pre.val = value
        else:
            node = self.ListNode(key, value)
            self.tail.pre.next = node
            node.pre = self.tail.pre
            node.next = self.tail
            self.tail.pre = node
            self.dicts[key] = node
            self.count += 1
            
if __name__ == '__main__':
    cache = LRUCache(2)
    # set(2,1),set(1,1),get(2),set(4,1),get(1),get(2)]
    cache.set(2, 1)
    cache.set(1, 1)
    cache.get(2)
    cache.set(4, 1)
    cache.get(1)
    cache.get(2)

