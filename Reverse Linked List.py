"""
Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The first node of the linked list.
    @return: You should return the head of the reversed linked list. 
                  Reverse it in-place.
    """
    def reverse(self, head):
        # write your code here
        # dummy = ListNode(-1)
        # cur = dummy
        # while head:
        #     tmp = head.next
        #     head.next = cur.next
        #     cur.next = head
        #     head = tmp
        # return dummy.next
        
        cur = None
        while head:
            tmp = head.next
            head.next = cur
            cur = head
            head = tmp
        return cur