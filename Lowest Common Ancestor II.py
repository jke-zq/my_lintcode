"""
Definition of ParentTreeNode:
class ParentTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None
"""
class Solution:
    """
    @param root: The root of the tree
    @param A and B: Two node in the tree
    @return: The lowest common ancestor of A and B
    """ 
    def lowestCommonAncestorII(self, root, A, B):
        # Write your code here
        
        parent = A
        hashP = set()
        while parent:
            hashP.add(parent)
            parent = parent.parent
        
        parent = B
        while parent:
            if parent in hashP:
                return parent
            else:
                parent = parent.parent
        return None
