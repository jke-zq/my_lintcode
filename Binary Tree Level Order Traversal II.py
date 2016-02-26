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
    @return: buttom-up level order in a list of lists of integers
    """
    def levelOrderBottom(self, root):
        # write your code here
        
        ret = []
        if not root:
            return []
        else:
            queue = [root]
            ret = []
            while queue:
                levelRet = []
                for __ in range(len(queue)):
                    node = queue.pop(0)
                    levelRet.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                ret.append(levelRet)
            return ret[::-1]