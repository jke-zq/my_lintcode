"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param head: The first node of linked list.
    @return: a tree node
    """
    def sortedListToBST(self, head):
        # write your code here
        
        # def helper(node, endNode):
        #     if not node or node == endNode:
        #         return None
            
        #     dummy = ListNode(0)
        #     dummy.next = node
        #     slow, fast = dummy, dummy
        #     while fast != endNode and fast.next != endNode:
        #         slow, fast = slow.next, fast.next.next
            
        #     root = TreeNode(slow.val)
        #     root.left = helper(node, slow)
        #     root.right = helper(slow.next, endNode)
        #     return root
        # return helper(head, None)
        
        # cur = head
        def helper(start, end):
            if start >= end:
                return None
            mid = start + (end - start) / 2
            left = helper(start, mid)
            # Using variable 'cur' before assignment (used-before-assignment)
            root = TreeNode(cur.val)
            root.left = left
            cur = cur.next
            root.right = helper(mid + 1, end)
            return root
            
        node = head
        length = 0
        while node:
            length, node = length + 1, node.next
        # self.cur = head
        return helper(0, length)