"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: A ListNode
    @return: A ListNode
    """
    def deleteDuplicates(self, head):
        # write your code here

        # dummy = ListNode(0)
        # p, q = head, None
        # head = dummy
        # while p:
        #     q = p
        #     while p.next and p.next.val == q.val:
        #         p = p.next
        #     if q == p:
        #         head.next, head = p, p
        #     p = p.next
        # ## error: next to all the left
        # head.next = None
        # return dummy.next
        
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                val = cur.next.val
                while cur.next and cur.next.val == val:
                    cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next
        # solution three
        # dummy = ListNode(0)
        # cur = dummy
        # pre = head
        # while pre:
        #     if pre.next and pre.val == pre.next.val:
        #         val = pre.val
        #         while pre and pre.val == val:
        #             pre = pre.next
        #     else:
        #         cur.next, cur = pre, pre
        #         pre = pre.next
        # cur.next = None
        # return dummy.next
##解题报告
# dummy Node 可以直接接着head，然后重新设置next指针
# 判断是否同一类的node，根据val的大小。
# 链表不断在后面添加next，注意最后node的next为None