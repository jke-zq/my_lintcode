# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param headA: the first list
    # @param headB: the second list
    # @return: a ListNode
    def getIntersectionNode(self, headA, headB):
        # Write your code here
        
        pA, pB = headA, headB
        tailA, tailB = False, False
        
        while pA and pB:
            if pA == pB:
                return pA
            
            pA = pA.next
            if not pA and not tailA:
                pA = headB
                tailA = True
            
            pB = pB.next
            if not pB and not tailB:
                pB = headA
                tailB = True
        
        return None