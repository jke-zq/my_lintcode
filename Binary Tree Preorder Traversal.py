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
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        # write your code here
        
        # def doTrav(node, ret):
        #     if not node:
        #         return
        #     else:
        #         ret.append(node.val)
        #         doTrav(node.left, ret)
        #         doTrav(node.right, ret)
        # ret = []
        # doTrav(root, ret)
        # return ret
                
        if not root:
            return []
        
        ret = []
        node = root
        stack = []
        while node:
            stack.append(node)
            ret.append(node.val)
            node = node.left
        while stack:
            node = stack.pop()
            # ret.append(node.val)
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    ret.append(node.val)
                    node = node.left
        return ret
        