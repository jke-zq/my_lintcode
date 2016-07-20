"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
import copy
class Solution:
    """
    @param root: The root of the binary search tree.
    @param A and B: two nodes in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """
    def lowestCommonAncestor(self, root, A, B):
        # write your code here
        if root in (None, A, B):
            return root
        # left, right = map(lambda x: self.lowestCommonAncestor(x, p, q), [root.left, root.right])
        left, right = map(lambda x: self.lowestCommonAncestor(x, A, B), [root.left, root.right])
        return root if left and right else left or right

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
import copy
class Solution:
    """
    @param root: The root of the binary search tree.
    @param A and B: two nodes in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """
    def lowestCommonAncestor(self, root, A, B):
        # write your code here

        # def helper(node, A, B):
        #     if node == None:
        #         return None
        #     if node == A or node == B:
        #         return node
        #     left = helper(node.left, A, B)
        #     right = helper(node.right, A, B)

        #     return node if left and right else left or right

        # return helper(root, A, B)

        def helper(node, target, paths):
            if not node:
                return False
            paths.append(node)
            if node.val == target.val:
                return True
            if node.left and helper(node.left, target, paths):
                return True
            if node.right and helper(node.right, target, paths):
                return True
            paths.pop()
            return False
        paths_a = []
        helper(root, A, paths_a)
        paths_b = []
        helper(root, B, paths_b)
        for p in paths_a[::-1]:
            if p in paths_b:
                return p
        return None



