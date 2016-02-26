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
    @return: A list of list of integer include 
             the zig zag level order traversal of its nodes' values
    """
    def zigzagLevelOrder(self, root):
        # write your code here
        
        ret = []
        if not root:
            return ret
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
        
        ##error: list[1::2]--list
        # ret[1::2] = ret[1::2][::-1]
        ret[1::2] = map(lambda x: x[::-1], ret[1::2])
        return ret