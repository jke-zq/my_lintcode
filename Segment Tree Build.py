"""
Definition of SegmentTreeNode:
class SegmentTreeNode:
    def __init__(self, start, end):
        self.start, self.end = start, end
        self.left, self.right = None, None
"""

class Solution:	
    # @param start, end: Denote an segment / interval
    # @return: The root of Segment Tree
    def build(self, start, end):
        # write your code here
        
        if start > end:
            return None
            
        node = SegmentTreeNode(start, end)
        if start == end:
            return node
        else:
            mid = start + (end - start) / 2
            node.left = self.build(start, mid)
            node.right = self.build(mid + 1, end)
            return node