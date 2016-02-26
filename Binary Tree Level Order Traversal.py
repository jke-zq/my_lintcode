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
    @return: Level order in a list of lists of integers
    """
    def levelOrder(self, root):
        # write your code here
        
        ret = []
        if not root:
            return ret
        else:
            queue = [root]
            while queue:
                # length = len(queue)
                level_val = []
                # while length:
                for i in range(len(queue)):
                    node = queue.pop(0)
                    level_val.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                    # length -= 1
                ret.append(level_val)
            return ret
                
                