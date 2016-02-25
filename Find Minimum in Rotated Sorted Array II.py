class Solution:
    # @param num: a rotated sorted array
    # @return: the minimum number in the array
    def findMin(self, num):
        # write your code here
        
        left, right = 0, len(num) - 1
        while left + 1 < right:
            while left + 1 < right and num[left] == num[right]:
                left += 1
            mid = left + (right - left) / 2
            if num[mid] <= num[right]:
                right = mid
            else:
                left = mid
        
        return min(num[left], num[right])