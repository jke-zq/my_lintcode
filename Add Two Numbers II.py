# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param l1: the first list
    # @param l2: the second list
    # @return: the sum list of l1 and l2 
    def addLists2(self, l1, l2):
        # Write your code here
        def reverse(root):
            cur = None
            while root:
                tmp = root.next
                root.next = cur
                cur = root
                root = tmp
            return cur
        
        l1 = reverse(l1)
        l2 = reverse(l2)
        
        dummy = ListNode(-1)
        cherry = 0
        cur = dummy
        while l1 or l2:
            v1 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            v2 = 0
            if l2:
                v2 = l2.val
                l2 = l2.next
                
            x = cherry + v1 + v2
            x, cherry = x % 10, x / 10
            cur.next = ListNode(x)
            cur = cur.next
        
        if cherry:
            cur.next = ListNode(cherry)
        
        l1 = reverse(l1)
        l2 = reverse(l2)
        
        ans = dummy.next
        ans = reverse(ans)
        return ans
            
            