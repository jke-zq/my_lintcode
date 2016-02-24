"""
Definition of SegmentTreeNode:
class SegmentTreeNode:
    def __init__(self, start, end, max):
        self.start, self.end, self.max = start, end, max
        self.left, self.right = None, None
"""

class Solution:	
    # @param root, start, end: The root of segment tree and 
    #                          an segment / interval
    # @return: The maximum number in the interval [start, end]
    def query(self, root, start, end):
        # write your code here
        
        if root.start > end or root.end < start:
            return float('-inf')
        else:
            if root.start >= start and root.end <= end:
                return root.max
            else:
                return max(self.query(root.left, start, end), self.query(root.right, start, end))