"""
Definition of ArrayReader:
class ArrayReader:
    def get(self, index):
        # this would return the number on the given index
        # if there is no number on that index, return -1
"""
class Solution:
    # @param {ArrayReader} reader: An instance of ArrayReader 
    # @param {int} target an integer
    # @return {int} an integer
    def searchBigSortedArray(self, reader, target):
        # write your code here
        
        if not reader:
            return -1
        
        k = 1
        while reader.get(k) != -1 and reader.get(k) < target:
            k *= 2
        left, right = 0, k
        while left + 1 < right:
            mid = left + (right - left) / 2
            if reader.get(mid) == -1 or reader.get(mid) >= target:
                right = mid
            elif reader.get(mid) < target:
                left = mid

        if reader.get(left) == target:
            return left
        if reader.get(right) != -1 and reader.get(right) == target:
            return right
        return -1