"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param root: The root of the binary search tree.
    @param k1 and k2: range k1 to k2.
    @return: Return all keys that k1<=key<=k2 in ascending order.
    """     
    def searchRange(self, root, k1, k2):
        # write your code here
        
        def helper(node, k1, k2, ret):
            if not node:
                return
            else:
                if node.val > k1:
                    helper(node.left, k1, k2, ret)
                if k1 <= node.val <= k2:
                    ret.append(node.val)
                if node.val < k2:
                    helper(node.right, k1, k2, ret)
                
        ret = []
        helper(root, k1, k2, ret)
        return ret