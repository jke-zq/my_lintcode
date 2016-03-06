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
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        # write your code here
        # def doTra(node, ret):
        #     if not node:
        #         return
        #     else:
        #         doTra(node.left, ret)
        #         ret.append(node.val)
        #         doTra(node.right, ret)
        
        # ret = []
        # doTra(root, ret)
        # return ret
        
        # ret = []
        # stack = []
        # node = root
        # while node:
        #     stack.append(node)
        #     node = node.left
        # while stack:
        #     node = stack.pop()
        #     ret.append(node.val)
        #     if node.right:
        #         node = node.right
        #         while node:
        #             stack.append(node)
        #             node = node.left
        # return ret
        if not root:
            return []
        stack, ret = [], []
        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            ret.append(cur.val)
            cur = cur.right
        return ret