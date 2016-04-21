"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """ 
    def minDepth(self, root):
        # write your code here
        
        def helper(node):
            if not node:
                return 0
            
            if not node.left and not node.right:
                return 1
            elif not node.left or not node.right:
                return 1 + max(helper(node.left), helper(node.right))
            else:
                return 1 + min(helper(node.left), helper(node.right))
        
        return helper(root)
                