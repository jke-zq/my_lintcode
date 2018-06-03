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
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):
        # write your code here

        ## traverse
        # def doCheck(node, minVal, maxVal):
        #     if not node:
        #         return True
        #     else:
        #         return minVal < node.val < maxVal and doCheck(node.left, minVal, node.val) and doCheck(node.right, node.val, maxVal)

        # return doCheck(root, float('-inf'), float('inf'))

        ## DC
        # def helper(node):
        #     if not node:
        #         return float('inf'), float('-inf'), True
        #     leftMin, leftMax, leftRet = helper(node.left)
        #     rightMin, rightMax, rightRet = helper(node.right)
        #     if not leftRet or not rightRet or node.val <= leftMax or node.val >= rightMin:
        #         return 0, 0, False
        #     retMin = min(leftMin, node.val)
        #     retMax = max(rightMax, node.val)
        #     return retMin, retMax, True

        # # if not root:
        # #     return True
        # __, __, ret = helper(root)
        # return ret
    def isValidBST(self, root):
        # write your code here
        def helper(node):
            if not node:
                return None, None, True
            leftMin, leftMax, leftRet = helper(node.left)
            rightMin, rightMax, rightRet = helper(node.right)
            # if not leftRet or not rightRet or node.val <= leftMax or node.val >= rightMin:
            #     return 0, 0, False
            # retMin = min(leftMin, node.val)
            # retMax = max(rightMax, node.val)
            if node.right and rightMin <= node.val:
                return 0, 0, False
            if node.left and leftMax >= node.val:
                return 0, 0, False
            if not leftRet or not rightRet:
                return 0, 0, False
            retMin = leftMin if node.left else node.val
            retMax = rightMax if node.right else node.val
            return retMin, retMax, True

        __, __, ret = helper(root)
        return ret

