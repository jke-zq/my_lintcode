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
    @return: The node where the cycle begins. 
                if there is no cycle, return null
    """
    def detectCycle(self, head):
        # write your code here
        
        # dummy = ListNode(-1)
        # dummy.next = head
        # fast, slow = dummy, dummy
        # while fast and fast.next:
        #     fast = fast.next.next
        #     slow = slow.next
        #     if slow == fast:
        #         break
        
        # if not fast or not fast.next:
        #     return None
        
        # slow = dummy
        # while slow != fast:
        #     slow = slow.next
        #     fast = fast.next
        # return slow

        #better codes
        if not head:
            return None

        fast, slow = head.next, head
        while fast != slow:
            if fast and fast.next:
                fast = fast.next.next
            else:
                return None
            slow = slow.next

        pre = head
        slow = slow.next
        while pre != slow:
            pre, slow = pre.next, slow.next
        return pre