# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        # Write your code here
        if not head or k == 0:
            return head
        
        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next
        times = length / k
        dummy = ListNode(0)
        # cur, end = head, dummy
        # for __ in range(times):
        #     next, tail, cur = cur, cur, cur.next
        #     next.next = None
        #     for __ in range(k - 1):
        #         cur.next, cur, next = next, cur.next, cur
        #     end.next, end = next, tail
        # end.next = cur
        tail = dummy
        cur = head
        for __ in range(times):
            next = cur
            for __ in range(k):
                tail.next, cur.next, cur = cur, tail.next, cur.next
            tail = next
        tail.next = cur
        return dummy.next
            
            