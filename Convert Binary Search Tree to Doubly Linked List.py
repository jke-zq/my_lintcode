"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
Definition of Doubly-ListNode
class DoublyListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = self.prev = next
"""

class Solution:
    """
    @param root, the root of tree
    @return: a doubly list node
    """
    def bstToDoublyList(self, root):
        # Write your code here
        
        def helper(treeNode):
            if not treeNode:
                return (None, None)
            
            (minLeft, maxLeft) = helper(treeNode.left)
            midle = DoublyListNode(treeNode.val)
            midle.pre = maxLeft
            if maxLeft:
                maxLeft.next = midle
            (minRight, maxRight) = helper(treeNode.right)
            midle.next = minRight
            if minRight:
                minRight.pre = midle
            minRet = midle if not minLeft else minLeft
            maxRet = midle if not maxRight else maxRight
            return (minRet, maxRet)
        
        return helper(root)[0]
            