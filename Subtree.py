"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    # @param T1, T2: The roots of binary tree.
    # @return: True if T2 is a subtree of T1, or false.
    def isSubtree(self, T1, T2):
        # write your code here
        # def check(t1, t2):
        #     ## import: the define of the subtree
        #     if t1 is None or t2 is None:
        #         return t1 == t2
        #     if t1.val == t2.val:
        #         return check(t1.left, t2.left) and check(t1.right, t2.right)
        #     else:
        #         return False
                
        # def helper(t1, t2):
        #     if not t1:
        #         return False
        #     if check(t1, t2):
        #         return True
        #     return helper(t1.left, t2) or helper(t1.right, t2)
        
        # if T2 is None:
        #     return True
        # return helper(T1, T2)
        
        def isEqual(t1, t2):
            if not t1 or not t2:
                return t1 == t2
            if t1.val != t2.val:
                return False
            else:
                return isEqual(t1.left, t2.left) and isEqual(t1.right, t2.right)
        
        if not T2:
            return True
        if not T1:
            return False
        if isEqual(T1, T2):
            return True
        else:
            return self.isSubtree(T1.left, T2) or self.isSubtree(T1.right, T2)
        