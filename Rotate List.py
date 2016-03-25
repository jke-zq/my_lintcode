# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head: the list
    # @param k: rotate to the right k places
    # @return: the list after rotation
    def rotateRight(self, head, k):
        # write your code here
        
        # if not head:
        #     return head
        # fast = head
        # length = 0
        # while fast:
        #     length += 1
        #     fast = fast.next
        # k = k % length
        # fast = head
        # for i in range(k):
        #     if not fast:
        #         return head
        #     fast = fast.next
        # slow = head
        # if not fast:
        #     return head
        # while fast.next:
        #     fast, slow = fast.next, slow.next
        # fast.next = head
        # head = slow.next
        # slow.next = None
        # return head
        def getLength(head):
            node = head
            length = 0
            while node:
                length += 1
                node = node.next
            return length
        
        if not head:
            return None
        length = getLength(head)
        k = k % length
        dummy = ListNode(0)
        dummy.next = head
        fast = dummy
        for i in range(k):
            fast = fast.next
            
        head = dummy
        while fast.next:
            head, fast = head.next, fast.next
        
        fast.next = dummy.next
        dummy.next = head.next
        head.next = None
        return dummy.next
        
        
