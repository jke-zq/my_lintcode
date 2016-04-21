"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
class Solution:
    """
    @param root, the root of binary tree.
    @return true if it is a complete binary tree, or false.
    """
    def isComplete(self, root):
        # Write your code here
        
        queue = [root]
        index = 0
        while index < len(queue):
            if queue[index]:
                queue.append(queue[index].left)
                queue.append(queue[index].right)
            index += 1
        
        ## queue is empty when root is None
        while queue and queue[-1] is None:
            queue.pop()
        
        for index in range(len(queue)):
            if queue[index] is None:
                return False
        
        return True
        
        