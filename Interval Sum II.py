class Solution:	
    class SegmentTree:
        def __init__(self, start, end, total):
            self.total = total
            self.start, self.end = start, end
            self.left, self.right = None, None
    def build(self, A):
        def doBuild(start, end, A):
            if start > end:
                return None
            if start == end:
                node = self.SegmentTree(start, end, A[start])
                return node
            node = self.SegmentTree(start, end, 0)
            mid = start + (end - start) / 2
            node.left = doBuild(start, mid, A)
            node.right = doBuild(mid + 1, end, A)
            node.total = node.left.total + node.right.total
            return node
            
        if not A:
            return None
        length = len(A)
        return doBuild(0, length - 1, A)
    # @param A: An integer list
    def __init__(self, A):
        # write your code here
        self.root = self.build(A)

    # @param start, end: Indices
    # @return: The sum from start to end
    def query(self, start, end):
        # write your code here
        def helper(node, start, end):
            if not node or node.start > end or node.end < start:
                return 0
            if node.start >= start and node.end <= end:
                return node.total
            return helper(node.left, start, end) + helper(node.right, start, end)
        return helper(self.root, start, end)
  
    # @param index, value: modify A[index] to value.
    def modify(self, index, value):
        # write your code here
        def helper(node, index, value):
            if not node:
                return 0
            if node.start > index or node.end < index:
                return node.total
            if node.start == index and node.end == index:
                node.total = value
                return value
            node.total = helper(node.left, index, value) + helper(node.right, index, value)
            return node.total
        return helper(self.root, index, value)
        