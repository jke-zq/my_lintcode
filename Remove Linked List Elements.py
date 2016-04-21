# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param val, an integer
    # @return a ListNode
    def removeElements(self, head, val):
        # Write your code here
        dummy = ListNode(-1)
        cur = dummy
        while head:
            if head.val != val:
                cur.next, cur = head, head
            head = head.next
        cur.next = None
        return dummy.next