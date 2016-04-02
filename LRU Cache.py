# class LRUCache:
#     class ListNode:
#         def __init__(self, key, value):
#             self.val = value
#             self.key = key
#             self.pre = None
#             self.next = None
#     # @param capacity, an integer
#     def __init__(self, capacity):
#         # write your code here
#         self.capacity = capacity
#         self.count = 0
#         self.root = self.ListNode(-1, -1)
#         self.tail = self.ListNode(-1, -1)
#         self.root.next = self.tail
#         self.tail.pre = self.root
#         self.dicts = {}

#     # @return an integer
#     def get(self, key):
#         #ListNode write your code here
#         if key in self.dicts:
#             ## delete from root
#             node = self.dicts[key]
#             self.root.next = node.next
#             self.root.next.pre = self.root
#             ## insert the tail
#             node.next = self.tail
#             self.tail.pre.next = node
#             node.pre = self.tail.pre
#             self.tail.pre = node
#             print node.val
#             return node.val
#         else:
#             print -1
#             return -1
        
#     # @param key, an integer
#     # @param value, an integer
#     # @return nothing
#     def set(self, key, value):
#         print key, value
#         # write your code here
#         if self.count >= self.capacity:
#             self.get(self.root.next.key)
#             self.dicts.pop(self.tail.pre.key)
#             self.tail.pre.key = key
#             self.tail.pre.val = value
#         else:
#             node = self.ListNode(key, value)
#             self.tail.pre.next = node
#             node.pre = self.tail.pre
#             node.next = self.tail
#             self.tail.pre = node
#             self.dicts[key] = node
#             self.count += 1
            
# if __name__ == '__main__':
#     cache = LRUCache(2)
#     # set(2,1),set(1,1),get(2),set(4,1),get(1),get(2)]
#     cache.set(2, 1)
#     cache.set(1, 1)
#     cache.get(2)
#     cache.set(4, 1)
#     cache.get(1)
#     cache.get(2)
class LRUCache:
    
    class Node:
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.next = None
    # @param capacity, an integer
    def __init__(self, capacity):
        # write your code here
        self.capa = capacity
        self.count = 0
        self.hashs = {}
        self.head = None
        self.tail = None

    # @return an integer
    def get(self, key):
        # write your code here
        if key not in self.hashs:
            return -1
        node = self.hashs[key]
        # print key, node.val
        if not node.next:
            return node.val
        nextnode = node.next
        # print nextnode.val, nextnode.key
        nextnode.val, node.val = node.val, nextnode.val
        nextnode.key, node.key = node.key, nextnode.key
        self.hashs[node.key] = node
        self.hashs[nextnode.key] = nextnode
        if self.tail == nextnode:
            return nextnode.val
        node.next = nextnode.next
        self.tail.next = nextnode
        nextnode.next = None
        self.tail = nextnode
        # print key, '----', nextnode.val
        return nextnode.val
        
    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        # write your code here
        if key in self.hashs:
            self.hashs[key].val = value
            self.get(key)
            return
        if self.count == self.capa:
            self.hashs.pop(self.head.key)
            self.head.val = value
            self.head.key = key
            self.hashs[key] = self.head
            # print self.head.key, self.head.val, 'ddd'
            self.get(key)
        else:
            node = LRUCache.Node(key, value)
            self.count += 1
            self.hashs[key] = node
            if not self.head:
                self.head = node
            if not self.tail:
                self.tail = node
            else:
                self.tail.next = node
                self.tail = node
            
