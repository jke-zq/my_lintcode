"""
Definition of SegmentTreeNode:
class SegmentTreeNode:
    def __init__(self, start, end, max):
        self.start, self.end, self.max = start, end, max
        self.left, self.right = None, None
"""

class Solution:	
    """
    @param root, index, value: The root of segment tree and 
    @ change the node's value with [index, index] to the new given value
    @return: nothing
    """
    def modify(self, root, index, value):
        # write your code here
        # if not root:
        #     return float('-inf')
        if root.start > index or root.end < index:
            return root.max
        if root.start == root.end == index:
            root.max = value
            return value
        else:
            root.max = (max(self.modify(root.right, index, value), 
                            self.modify(root.left, index, value)))
            return root.max