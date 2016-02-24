"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class SegNode:
    def __init__(self, start, end):
        self.start, self.end, self.min = start, end, None
        self.left, self.right = None, None
        
class Solution:	
    """
    @param A, queries: Given an integer array and an Interval list
                       The ith query is [queries[i-1].start, queries[i-1].end]
    @return: The result list
    """
    def intervalMinNumber(self, A, queries):
        # write your code here
        def doBuild(left, right):
            node = SegNode(left, right)
            if left == right:
                node.min = A[left]
                return node
            else:
                mid = left + (right - left) / 2
                node.left = doBuild(left, mid)
                node.right = doBuild(mid + 1, right)
                node.min = min(node.left.min, node.right.min)
                return node
        def doQuery(node, start, end):
            if node.start > end or node.end < start:
                return float('inf')
            else:
                if node.start >= start and node.end <= end:
                    return node.min
                else:
                    return min(doQuery(node.left, start, end), doQuery(node.right, start, end))
        
        root = doBuild(0, len(A) - 1)
        ret = []
        for q in queries:
            ret.append(doQuery(root, q.start, q.end))
        return ret
            