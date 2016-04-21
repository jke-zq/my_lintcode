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
    @return true if it is a mirror of itself, or false.
    """
    def isSymmetric(self, root):
        # Write your code here
        
        ## Traverse
        # def helper(na, nb):
        #     if not na and not nb:
        #         return True
        #     if na and nb and na.val == nb.val:
        #         return helper(na.left, nb.right) and helper(na.right, nb.left)
        #     else:
        #         return False
        
        # if not root:
        #     return True
        # return helper(root.left, root.right)
        
        ## iterator
        if not root:
            return True
        queue = [root.left, root.right]
        while queue:
            for __ in range(len(queue) / 2):
                left, right = queue.pop(0), queue.pop(0)
                if not left and not right:
                    continue
                if left and right and left.val == right.val:
                    queue.append(left.left)
                    queue.append(right.right)
                    queue.append(left.right)
                    queue.append(right.left)
                else:
                    return False
        return True