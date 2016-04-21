"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    # @param head: the head of linked list.
    # @return: a middle node of the linked list
    def middleNode(self, head):
        # Write your code here
        if not head:
            return None
        dummy = ListNode(-1)
        dummy.next = head
        fast, slow = dummy, dummy
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
        return slow
        