"""
Definition of SegmentTreeNode:
class SegmentTreeNode:
    def __init__(self, start, end, max):
        self.start, self.end, self.max = start, end, max
        self.left, self.right = None, None
"""

class Solution:	
    # @oaram A: a list of integer
    # @return: The root of Segment Tree
    def build(self, A):
        # write your code here
        
        def doBuild(left, right):
            #if left > right:
            #    return None
            node = SegmentTreeNode(left, right)
            if left == right:
                node.max = A[left]
                return node
            else:
                mid = left + (right - left) / 2
                node.left = doBuild(left, mid)
                node.right = doBuild(mid + 1, right)
                node.max = max(node.left.max, node.right.max)
                return node
        if not A:
            return None
        return doBuild(0, len(A) - 1)