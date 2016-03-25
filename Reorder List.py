"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The first node of the linked list.
    @return: nothing
    """
    def reorderList(self, head):
        # write your code here
        
        dummy = ListNode(0)
        dummy.next = head
        slow, fast = dummy, dummy
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        
        tail, slow.next = slow.next, None
        newhead = None
        while tail:
            tmp, tail = tail, tail.next
            tmp.next = newhead
            newhead = tmp
        head = dummy.next
        ans = dummy
        while head:
            dummy.next, head, dummy = head, head.next, head
            dummy.next, newhead, dummy = newhead, newhead.next, newhead
        return ans.next
