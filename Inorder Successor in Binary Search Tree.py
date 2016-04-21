# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    """
    @param root <TreeNode>: The root of the BST.
    @param p <TreeNode>: You need find the successor node of p.
    @return <TreeNode>: Successor of p.
    """
    def inorderSuccessor(self, root, p):
        # write your code here
        
        # if not root:
        #     return None

        # if p.right:
        #     node = p.right
        #     while node and node.left:
        #         node = node.left
        #     return node
        # else:
        #     nodes = []
        #     node = root
        #     while node.val != p.val:
        #         nodes.append(node)
        #         if node.val < p.val:
        #             node = node.right
        #         else:
        #             node = node.left
        #     for n in nodes[::-1]:
        #         if n.val > p.val:
        #             return n
        #     return None

              
        preLeft = None
        cur = root
        while cur and cur.val != p.val:
            if cur.val > p.val:
                preLeft = cur
                cur = cur.left
            else:
                cur = cur.right
        
        if not cur:
            return None
        if p.right:
            cur = p.right
            while cur.left:
                cur = cur.left
            return cur
        if preLeft:
            return preLeft
        ## the last one
        return None
        
        
                    