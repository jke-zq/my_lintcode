"""
Definition of SegmentTreeNode:
class SegmentTreeNode:
    def __init__(self, start, end, count):
        self.start, self.end, self.count = start, end, count
        self.left, self.right = None, None
"""

class Solution:	
    # @param root, start, end: The root of segment tree and 
    #                          an segment / interval
    # @return: The count number in the interval [start, end] 
    def query(self, root, start, end):
        # write your code here
        if not root or root.start > end or root.end < start:
            return 0
        if root.start >= start and root.end <= end:
            return root.count
        
        return self.query(root.left, start, end) + self.query(root.right, start, end)