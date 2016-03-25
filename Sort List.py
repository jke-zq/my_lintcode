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
    @return: You should return the head of the sorted linked list,
                  using constant space complexity.
    """
    def sortList(self, head):
        # write your code here
        def merge(list1, list2):
            dummy = ListNode(0)
            head = dummy
            while list1 and list2:
                if list1.val < list2.val:
                    head.next, head = list1, list1
                    list1 = list1.next
                else:
                    head.next, head = list2, list2
                    list2 = list2.next
            
            if list1:
                head.next = list1
            if list2:
                head.next = list2
            return dummy.next
        
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        slow, fast = dummy, dummy
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        newhead = slow.next
        ## error: must be
        slow.next = None
        list1 = self.sortList(dummy.next)
        list2 = self.sortList(newhead)
        return merge(list1, list2)


## quick sort
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def sort(start):
            if not start or not start.next:
                return (start, start)
            pivot = start.val
            pivotNode = start
            start = start.next
            pivotNode.next = None
            
            leftDummy = ListNode(0)
            rightDummy = ListNode(0)
            midDummy = ListNode(0)
            midDummy.next = pivotNode
            left, right, mid = leftDummy, rightDummy, pivotNode
            while start:
                if start.val < pivot:
                    left.next, left = start, start
                elif start.val == pivot:
                    mid.next, mid = start, start
                else:
                    right.next, right = start, start
                start = start.next
            
            ## do Recurstion
            left.next, mid.next, right.next = None, None, None
            
            retStart = midDummy.next
            retEnd = mid
            leftResult = sort(leftDummy.next)
            if leftResult[1]:
                retStart, leftResult[1].next = leftResult[0], midDummy.next
            rightResult = sort(rightDummy.next)
            if rightResult[0] != None:
                mid.next, retEnd = rightResult
            return (retStart, retEnd)
        
        return sort(head)[0]