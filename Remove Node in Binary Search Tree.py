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
    @param value: Remove the node with given value.
    @return: The root of the binary search tree after removal.
    """    
    def removeNode(self, root, value):
        # write your code here
        
        if not root:
            return
        else:
            if root.val > value:
                root.left = self.removeNode(root.left, value)
                return root
            elif root.val < value:
                root.right = self.removeNode(root.right, value)
                return root
            else:
                if not root.right:
                    return root.left
                # elif not root.left:
                #     return root.right
                else:
                    pre, cur = None, root.right
                    while cur and cur.left:
                        pre, cur = cur, cur.left
                    if pre:
                        pre.left = cur.right
                    else:
                        root.right = cur.right
                    cur.left, cur.right = root.left, root.right
                    return cur
            
