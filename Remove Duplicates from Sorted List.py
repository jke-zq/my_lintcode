"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: A ListNode
    @return: A ListNode
    """
    def deleteDuplicates(self, head):
        # write your code here
        dummy = ListNode(float('-inf'))
        cur = dummy
        while head:
            if head.val != cur.val:
                cur.next = head
                cur = head
            head = head.next
        cur.next = None
        return dummy.next