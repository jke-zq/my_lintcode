"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param root: The root of the binary search tree.
    @param node: insert this node into the binary search tree.
    @return: The root of the new binary search tree.
    """
    def insertNode(self, root, node):
        # write your code here
        
        p = root
        while p:
            pre = p
            if p.val > node.val:
                if not p.left:
                    p.left = node
                    return root
                else:
                    p = p.left
            else:
                if not p.right:
                    p.right = node
                    return root
                else:    
                    p = p.right
        return node