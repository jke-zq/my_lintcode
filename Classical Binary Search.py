class Solution:
    # @param {int[]} A an integer array sorted in ascending order
    # @param {int} target an integer
    # @return {int} an integer
    def findPosition(self, A, target):
        # Write your code here
        
        if not A:
            return -1
        length = len(A)
        left, right = 0, length - 1
        while left + 1< right:
            mid = left + (right - left) / 2
            if A[mid] > target:
                right = mid
            elif A[mid] < target:
                left = mid
            else:
                return mid
        if A[left] == target:
            return left
        elif A[right] == target:
            return right
        else:
            return -1
                