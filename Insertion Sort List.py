"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The first node of linked list.
    @return: The head of linked list.
    """ 
    def insertionSortList(self, head):
        # write your code here
        def insert(dummy, node):
            cur = dummy
            while cur.next:
                if cur.next.val < node.val:
                    cur = cur.next
                else:
                    tmp = cur.next
                    cur.next = node
                    node.next = tmp
                    return dummy
            cur.next = node
            # node.next = None
            return dummy
        
        def judge(root):
            cur = root
            while cur.next:
                if cur.val < cur.next.val:
                    cur = cur.next
                else:
                    return False
            return True
        
        
        if judge(head):
            return head
            
        dummy = ListNode(0)
        cur = head
        while cur:
            tmp = cur
            cur = cur.next
            tmp.next = None
            insert(dummy, tmp)
        return dummy.next