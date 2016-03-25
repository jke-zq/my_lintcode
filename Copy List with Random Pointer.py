# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        # write your code here
        
        # ## copy
        # cur = head
        # while cur:
        #     next = cur.next
        #     cur.next = RandomListNode(cur.label)
        #     cur.next.next = next
        #     cur = next
        
        # ## copy random
        # cur = head
        # while cur:
        #     if cur.random:
        #         cur.next.random = cur.random.next
        #     cur = cur.next.next
            
        # ## sperate
        # cur, ans = head, head.next
        # ansCur = ans
        # while cur:
        #     cur.next, cur = cur.next.next, cur.next.next
        #     if ansCur.next:
        #         ansCur.next, ansCur = ansCur.next.next, ansCur.next.next
        # return ans
        
        dummy = RandomListNode(0)
        newCur, cur = dummy, head
        dict = {}
        while cur:
            newCur.next = RandomListNode(cur.label)
            newCur = newCur.next
            dict[cur] = newCur
            cur = cur.next
        
        ## copy random
        cur = head
        newCur = dummy.next
        while cur:
            if cur.random:
                newCur.random = dict[cur.random]
            cur, newCur = cur.next, newCur.next
        return dummy.next
        
        