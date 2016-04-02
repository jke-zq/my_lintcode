class Dequeue(object):
    class Node:
        def __init__(self, val):
            self.val = val
            self.next = None
            self.pre = None
            
    def __init__(self):
        # do some intialize if necessary
        self.head = Dequeue.Node(0)
        self.tail = self.head

    # @param {int} item an integer
    # @return nothing
    def push_front(self, item):
        # Write yout code here
        node = Dequeue.Node(item)
        node.next = self.head.next
        if self.head.next:
            self.head.next.pre = node
        else:
            self.tail = node
        node.pre = self.head
        self.head.next = node

    # @param {int} item an integer
    # @return nothing
    def push_back(self, item):
        # Write yout code here
        node = Dequeue.Node(item)
        self.tail.next = node
        node.pre = self.tail
        self.tail = node

    # @return an integer
    def pop_front(self):
        # Write your code here
        node = self.head.next
        self.head.next = node.next
        if not node.next:
            self.tail = self.head
        else:
            node.next.pre = self.head
        return node.val

    # @return an integer
    def pop_back(self):
        # Write your code here
        node = self.tail
        self.tail = node.pre
        self.tail.next = None
        return node.val