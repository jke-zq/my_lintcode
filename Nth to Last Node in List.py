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
    @param n: An integer.
    @return: Nth to last node of a singly linked list. 
    """
    def nthToLast(self, head, n):
        # write your code here
        if not head:
            return head
        dummy = ListNode(0)
        dummy.next = head
        fast = dummy
        for __ in range(n):
            fast = fast.next
        
        slow = dummy
        while fast.next:
            fast, slow = fast.next, slow.next
        return slow.next