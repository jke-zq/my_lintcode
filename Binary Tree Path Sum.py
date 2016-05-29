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
        def travel(sumVal, node, tmp, ans, target):
            if not node:
                return
            sumVal += node.val
            tmp.append(node.val)
            if not node.left and not node.right and sumVal == target:
                ans.append(tmp[:])
                ## Dont forget to pop the val
                tmp.pop()
                return
            travel(sumVal, node.left, tmp, ans, target)
            travel(sumVal, node.right, tmp, ans, target)
            tmp.pop()
        
        if not root:
            return []
        
        ans, tmp = [], []
        travel(0, root, tmp, ans, target)
        return ans
        
        ## this is wrong solution: from root to any node of the tree
        # def traverse(node, target, tmp, sumVal, ret):
        #     if not node:
        #         return 
        #     sumVal += node.val
        #     tmp.append(node.val)
        #     if sumVal == target:
        #         ret.append(tmp[:])
        #     traverse(node.left, target, tmp, sumVal, ret)
        #     traverse(node.right, target, tmp, sumVal, ret)
        #     sumVal -= node.val
        #     tmp.pop()

        
        # ret, tmp = [], []
        # traverse(root, target, tmp, 0, ret)
        # return ret