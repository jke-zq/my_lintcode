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
    @return: True if the binary tree is BST, or false
    """  
    def isValidBST(self, root):
        # write your code here
        
        def doCheck(node, minVal, maxVal):
            if not node:
                return True
            else:
                return minVal < node.val < maxVal and doCheck(node.left, minVal, node.val) and doCheck(node.right, node.val, maxVal)
        
        return doCheck(root, float('-inf'), float('inf'))