# class Comparator:
#     def cmp(self, a, b)
# You can use Compare.cmp(a, b) to compare nuts "a" and bolts "b",
# if "a" is bigger than "b", it will return 1, else if they are equal,
# it will return 0, else if "a" is smaller than "b", it will return -1.
# When "a" is not a nut or "b" is not a bolt, it will return 2, which is not valid.
import random
class Solution:
    # @param nuts: a list of integers
    # @param bolts: a list of integers
    # @param compare: a instance of Comparator
    # @return: nothing
    def sortNutsAndBolts(self, nuts, bolts, compare):
        # write your code here
        def helper(left, right, nuts, bolts, compare):
            if left >= right:
                return
            boltIndex = random.randint(left, right)
            target = nuts[boltIndex]
            l, pivot, r = left, left, right
            while l <= r:
                if compare.cmp(target, bolts[l]) == 1:
                    bolts[l], bolts[r] = bolts[r], bolts[l]
                    r -= 1
                elif compare.cmp(target, bolts[l]) == 0:
                    l += 1
                else:
                    bolts[l], bolts[pivot] = bolts[pivot], bolts[l]
                    pivot += 1
                    l += 1
                    
            target = bolts[pivot]
            l, pivot, r = left, left, right
            while l <= r:
                if compare.cmp(nuts[l], target) == -1:
                    nuts[l], nuts[r] = nuts[r], nuts[l]
                    r -= 1
                elif compare.cmp(nuts[l], target) == 0:
                    l += 1
                else:
                    nuts[l], nuts[pivot] = nuts[pivot], nuts[l]
                    pivot += 1
                    l += 1
            helper(left, pivot - 1, nuts, bolts, compare)
            helper(pivot + 1, right, nuts, bolts, compare)
        
        if not nuts:
            return
        length = len(nuts)
        helper(0, length - 1, nuts, bolts, compare)
                    
                    