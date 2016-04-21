# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head, a ListNode
    # @oaram {int} v1 an integer
    # @param {int} v2 an integer
    # @return {ListNode} a new head of singly-linked list
    def swapNodes(self, head, v1, v2):
        # Write your code here
        
        dummy = ListNode(-1)
        dummy.next = head
        cur = dummy
        prev1, prev2 = None, None
        while cur.next:
            if cur.next.val == v1:
                prev1 = cur
            elif cur.next.val == v2:
                prev2 = cur
            cur = cur.next
        if prev1 and prev2:
            node1 = prev1.next
            node2 = prev2.next
            prev1.next = node2
            prev2.next = node1
            node2.next, node1.next = node1.next, node2.next
        return dummy.next
        
