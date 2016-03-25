"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    # @param A: Given an integer array with no duplicates.
    # @return: The root of max tree.
    def maxTree(self, A):
        # write your code here
        
        if not A:
            return None
        
        stack = []
        A.append(float('inf'))
        for a in A:
            if not stack or stack[-1].val > a:
                stack.append(TreeNode(a))
            else:
                cur = stack.pop()
                while stack and stack[-1].val < a:
                    node = stack.pop()
                    node.right = cur
                    cur = node

                node = TreeNode(a)
                node.left = cur
                stack.append(node)
        return stack[0].left
                        
        