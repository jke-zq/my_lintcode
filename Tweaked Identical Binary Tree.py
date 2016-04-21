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
    @return true if they are tweaked identical, or false.
    """
    def isTweakedIdentical(self, a, b):
        # Write your code here
        
        def helper(nodea, nodeb):
            
            if not nodea and not nodeb:
                return True
            if nodea and nodeb and nodea.val == nodeb.val:
                return (helper(nodea.left, nodeb.right) and helper(nodea.right, nodeb.left)) or (helper(nodea.left, nodeb.left) and helper(nodea.right, nodeb.right))
            else:
                return False
        
        return helper(a, b)