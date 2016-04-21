"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param preorder : A list of integers that preorder traversal of a tree
    @param inorder : A list of integers that inorder traversal of a tree
    @return : Root of a tree
    """
    def buildTree(self, preorder, inorder):
        # write your code here
        def helper(prestart, preend, perorder, instart, inend, inorder):
            if prestart > preend:
                return None
            
            node = TreeNode(preorder[prestart])
            index = inorder.index(node.val)
            node.left = helper(prestart + 1, index - instart + prestart, preorder, instart, index - 1, inorder)
            node.right = helper(index - instart + prestart + 1, preend, preorder, index + 1, inend, inorder)
            return node
        return helper(0, len(preorder) - 1, preorder, 0, len(inorder) - 1, inorder)