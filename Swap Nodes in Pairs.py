# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        # Write your code here
        dummy = ListNode(0)
        cur = dummy
        while head and head.next:
            tmp = head.next.next
            cur.next = head.next
            cur.next.next = head
            cur = head
            head = tmp
        cur.next = head
        return dummy.next
            