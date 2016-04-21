"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
class Solution:
    """
    @param a, b, the root of binary trees.
    @return true if they are identical, or false.
    """
    def isIdentical(self, a, b):
        # Write your code here
        def helper(na, nb):
            if not na and not nb:
                return True
            if na and nb and na.val == nb.val:
                return helper(na.left, nb.left) and helper(na.right, nb.right)
            else:
                return False
        
        return helper(a, b)