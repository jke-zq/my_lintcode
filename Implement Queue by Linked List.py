class MyQueue(object):
    class Node:
        def __init__(self, val):
            self.val = val
            self.next = None
            
    def __init__(self):
        # do some intialize if necessary
        self.head = MyQueue.Node(0)
        self.tail = self.head

    # @param {int} item an integer
    # @return nothing
    def enqueue(self, item):
        # Write yout code here
        node = MyQueue.Node(item)
        self.tail.next = node
        self.tail = node

    # @return an integer
    def dequeue(self):
        # Write your code here
        node = self.head.next
        self.head.next = node.next
        if node == self.tail:
            self.tail = self.head
        return node.val