"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param inorder : A list of integers that inorder traversal of a tree
    @param postorder : A list of integers that postorder traversal of a tree
    @return : Root of a tree
    """
    def buildTree(self, inorder, postorder):
        # write your code here
        def helper(instart, inend, inorder, poststart, postend, postorder):
            if poststart > postend:
                return None
            
            node = TreeNode(postorder[postend])
            index = inorder.index(node.val)
            node.left = helper(instart, index - 1, inorder, poststart, poststart + index - instart - 1, postorder)
            node.right = helper(index + 1, inend, inorder, poststart + index - instart, postend - 1, postorder)
            return node
        
        return helper(0, len(inorder) - 1, inorder, 0, len(postorder) - 1, postorder)