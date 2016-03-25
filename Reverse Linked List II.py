"""
Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The head of linked list
    @param m: start position
    @param n: end position
    """
    def reverseBetween(self, head, m, n):
        # write your code here
        
        dummy = ListNode(0)
        left = dummy
        dummy.next = head
        for i in range(m - 1):
            left = left.next
        right = left.next
        end = right
        for i in range(n - m + 1):
            # error:dont use this
            # right.next, left.next, right = left.next, right, right.next
            tmp = right
            right = right.next
            tmp.next = left.next
            left.next = tmp
        end.next = right
        return dummy.next
