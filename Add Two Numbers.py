# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param l1: the first list
    # @param l2: the second list
    # @return: the sum list of l1 and l2 
    def addLists(self, l1, l2):
        # write your code here
        dummy = ListNode(0)
        cur = dummy
        cherry = 0
        while l1 or l2:
            v1 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            # v2 = l2.val if l2 else 0
            v2 = 0
            if l2:
                v2 = l2.val
                l2 = l2.next
            x = cherry + v1 + v2
            cherry = x / 10
            x = x % 10
            cur.next = ListNode(x)
            cur = cur.next
        
        if cherry:
            cur.next = ListNode(cherry)
        
        return dummy.next