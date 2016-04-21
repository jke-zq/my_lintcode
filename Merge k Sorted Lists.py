"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
import heapq
class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        # write your code here
        ## using heap
        # heap = []
        # for node in lists:
        #     if node:
        #         heap.append((node.val, node))
            
        # heapq.heapify(heap)
        # dummy = ListNode(0)
        # cur = dummy
        # while heap:
        #     __, node = heapq.heappop(heap)
        #     cur.next, cur = node, node
        #     if node.next:
        #         heapq.heappush(heap, (node.next.val, node.next))
        # return dummy.next
        
        ## using DC
        # def doMerge(lists, start, end):
        #     if start > end:
        #         return None
        #     if start == end:
        #         return lists[start]
        #     mid = start + (end - start) / 2
        #     list1 = doMerge(lists, start, mid)
        #     list2 = doMerge(lists, mid + 1, end)
            
        #     ## merge
        #     dummy = ListNode(0)
        #     cur = dummy
        #     while list1 and list2:
        #         if list1.val < list2.val:
        #             cur.next, cur, list1 = list1, list1, list1.next
        #         else:
        #             cur.next, cur, list2 = list2, list2, list2.next
        #     if list1:
        #         cur.next = list1
        #     if list2:
        #         cur.next = list2
                
        #     return dummy.next
            
        # if not lists:
        #     return None
        # length = len(lists)
        # return doMerge(lists, 0, length - 1)
        
        ## using DC without Recursion
        if not lists:
            return None
            
        dummy = ListNode(0)
        listNode = lists[:]
        while len(listNode) > 1:
            length = len(listNode)
            while length > 1:
                    list1, list2 = listNode.pop(0), listNode.pop(0)
                    length -= 2
                    cur = dummy
                    
                    while list1 and list2:
                        if list1.val < list2.val:
                            cur.next, cur, list1 = list1, list1, list1.next
                        else:
                            cur.next, cur, list2 = list2, list2, list2.next
                    if list1:
                        cur.next = list1
                    if list2:
                        cur.next = list2
                    listNode.append(dummy.next)
                    # dummy.next = None
            # if length == 1:
            #     listNode.append(listNode.pop(0))
        return listNode[0]