"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The first node of linked list.
    @param x: an integer
    @return: a ListNode 
    """
    def partition(self, head, x):
        # write your code here
        
        left = ListNode(0)
        p = left
        right = ListNode(0)
        q = right
        while head:
            if head.val < x:
                p.next = head
                p = p.next
            else:
                q.next, q = head, head
            head = head.next
        
        p.next = right.next
        ## error
        q.next = None
        return left.next