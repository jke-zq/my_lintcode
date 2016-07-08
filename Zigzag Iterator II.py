class ZigzagIterator2:
    class ListNode:
        def __init__(self, id_, index, length):
            self.index = index
            self.id_ = id_
            self.length = length
            self.pre, self.next = None, None

    # @param {int[][]} a list of 1d vectors
    def __init__(self, vecs):
        # initialize your data structure here
        self.vecs = vecs
        self.start = ZigzagIterator2.ListNode(0, 0, 0)
        self.pre = self.start
        for i, v in enumerate(self.vecs):
            length = len(v)
            # error
            if length == 0:
                continue
            node = ZigzagIterator2.ListNode(i, 0, length)
            self.pre.next = node
            node.pre = self.pre
            self.pre = node
        # error
        if self.pre != self.start:
            self.pre.next = self.start.next
            self.start.next.pre = self.pre
        self.start = self.start.next

    def next(self):
        # Write your code here
        val = self.vecs[self.start.id_][self.start.index]
        if self.start.index + 1 < self.start.length:
            self.start.index += 1
            # error
            self.start = self.start.next
        else:
            if self.start.next == self.start:
                self.start = None
            else:
                pre, next_ = self.start.pre, self.start.next
                pre.next, next_.pre = next_, pre
                # error
                self.start = self.start.next
                # self.start.pre.next = self.start.next
                # self.start.next.pre = self.start.pre
                # self.start = self.start.next
        return val

    def hasNext(self):
        # Write your code here
        return self.start is not None

# Your ZigzagIterator2 object will be instantiated and called as such:
# solution, result = ZigzagIterator2(vecs), []
# while solution.hasNext(): result.append(solution.next())
# Output result
