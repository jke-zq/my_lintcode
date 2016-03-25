"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param hashTable: A list of The first node of linked list
    @return: A list of The first node of linked list which have twice size
    """
    def rehashing(self, hashTable):
        # write your code here
        def add(node, newTable, hashFunc):
            
            if node:
                index = hashFunc(node.val)
                if newTable[index]:
                    root = newTable[index]
                    while root.next:
                        root = root.next
                    root.next = ListNode(node.val)
                    
                else:
                    root = ListNode(node.val)
                    newTable[index] = root
            
        length = len(hashTable) * 2
        newTable = [None] * length
        hashFunc = lambda x: x % length
        for i in range(length / 2):
            if hashTable[i]:
                root = hashTable[i]
                while root:
                    add(root, newTable, hashFunc)
                    root = root.next
        return newTable
