"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    # @param {TreeNode} root the root of the binary tree
    # @return {List[str]} all root-to-leaf paths
    def binaryTreePaths(self, root):
        # Write your code here
        
        
        def helper(node, tmp, ret):
            # if not node:
            #     return
            # else:
            #     tmp.append(str(node.val))
            #     if not node.left and not node.right:
            #         ret.append('->'.join(tmp))
            #     helper(node.left, tmp, ret)
            #     helper(node.right, tmp, ret)
            #     tmp.pop()
            if not node:
                return
            if not node.left and not node.right:
                ret.append(tmp)
            if node.left:
                helper(node.left, tmp + '->' + str(node.left.val), ret)
            if node.right:
                helper(node.right, tmp + '->' + str(node.right.val), ret)
                
        if not root:
            return []
        tmp, ret = str(root.val), []
        helper(root, tmp, ret)
        return ret
