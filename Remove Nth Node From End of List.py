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
    @return: The head of linked list.
    """
    def removeNthFromEnd(self, head, n):
        # write your code here
        dummy = ListNode(-1)
        dummy.next = head
        fast = dummy
        for __ in range(n):
            fast = fast.next
        slow = dummy
        while fast.next:
            fast, slow = fast.next, slow.next
        
        slow.next = slow.next.next
        return dummy.next


## new solution and solid codes
    def removeNthFromEnd(self, head, n):
        # write your code here
        if not head:
            return None
        if n <= 0:
            return head
        
        # check if n <= length
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        
        if length < n:
            return head
        
        if n == length:
            return head.next
            
        n = length - n + 1 - 1
        cur = head
        # while n > 1:
        for __ in range(n - 1):
            cur = cur.next
        cur.next = cur.next.next
        return head