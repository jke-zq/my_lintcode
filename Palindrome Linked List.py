# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def isPalindrome(self, head):
        # Write your code here
        
        def reverse(root):
            cur = None
            while root:
                tmp = root.next
                root.next = cur
                cur = root
                root = tmp
            return cur
        
        if not head:
            return True
            
        dummy = ListNode(-1)
        dummy.next = head
        fast, slow = dummy, dummy
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
        
        nextHead = slow.next
        nextHead = reverse(nextHead)
        cur = nextHead
        ans = True
        while cur:
            if head.val == cur.val:
                head = head.next
                cur = cur.next
            else:
                ans = False
                break
        
        ## recover the data
        nextHead = reverse(nextHead)
        head = dummy.next
        slow.next = nextHead
        return ans