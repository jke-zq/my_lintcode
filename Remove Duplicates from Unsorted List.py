"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def removeDuplicates(self, head):
        # Write your code here
        
        dummy = ListNode(0)
        cur = dummy
        vals = set()
        while head:
            if head.val not in vals:
                vals.add(head.val)
                cur.next = head
                cur = head
            head = head.next
        cur.next = None
        return dummy.next