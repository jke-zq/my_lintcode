"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    # @param {TreeNode} root the root of binary tree
    # @param {int} target an integer
    # @return {int[][]} all valid paths
    def binaryTreePathSum(self, root, target):
        # Write your code here
        
        def traverse(node, target, tmp, sumVal, ret):
            if not node:
                return 
            sumVal += node.val
            tmp.append(node.val)
            if sumVal == target:
                ret.append(tmp[:])
            traverse(node.left, target, tmp, sumVal, ret)
            traverse(node.right, target, tmp, sumVal, ret)
            sumVal -= node.val
            tmp.pop()

        
        ret, tmp = [], []
        traverse(root, target, tmp, 0, ret)
        return ret