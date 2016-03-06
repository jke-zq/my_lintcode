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
    @return: An integer
    """
    def maxPathSum(self, root):
        # write your code here
        # def helper(root):
        #     if not root:
        #         return float('-inf'), float('-inf')
        #     else:
        #         (left, left_max), (right, right_max) = map(lambda x: helper(x), [root.left, root.right])
        #         leaf = max(left, right)
        #         cur = max(leaf + root.val, root.val)
        #         return (cur, max(cur, left_max, right_max, root.val + left + right))
        
        # __, ret = helper(root)
        # return ret
        
        def helper(root):
            if not root:
                ## error: 0 used to add, float('-inf') used to be compared
                return 0, float('-inf')
            
            left = helper(root.left)
            right = helper(root.right)
            ## error: just to decide to add the root or not.
            siglepath = max(left[0] + root.val, right[0] + root.val, 0)
            maxpath = max(left[1], right[1], left[0] + root.val + right[0])
            return siglepath, maxpath
        __, ret = helper(root)
        return ret
            
            
                