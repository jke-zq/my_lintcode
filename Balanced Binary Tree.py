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
    @return: True if this Binary tree is Balanced, or false.
    """
    def isBalanced(self, root):
        # write your code here
        
        def helper(root):
            if not root:
                return 0
            else:
                left = helper(root.left)
                if left == -1:
                    return -1
                else:
                    right = helper(root.right)
                    if right == -1:
                        return -1
                    elif abs(left - right) > 1:
                        return -1
                    else:
                        return max(left, right) + 1
        
        return helper(root) != -1