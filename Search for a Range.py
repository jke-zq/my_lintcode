class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        # write your code here
        if not A:
            return [-1, -1]
            
        ret = [-1, -1]
        left, right = 0, len(A) - 1
        while left + 1 < right:
            mid = left + (right - left) / 2
            if A[mid] >= target:
                right = mid
            else:
                left = mid
                
        if A[left] == target:
            ret[0] = left
        elif A[right] == target:
            ret[0] = right

        
        left, right = 0, len(A) - 1
        while left + 1 < right:
            mid = left + (right - left) / 2
            if A[mid] > target:
                right = mid
            else:
                left = mid
                
        ##error
        # if A[left] == target:
        #     ret[1] = left
        # if A[right] == target:
        #     ret[1] = right
        if A[right] == target:
            ret[1] = right
        elif A[left] == target:
            ret[1] = left

        return ret
if __name__ == '__main__':
    print Solution().searchRange([1,2 , 4], 8)

## solution 2: using recursion
class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        # write your code here
        def helper(start, end, A):
            if start > end:
                return [float('inf'), float('-inf')]
            if A[start] == target and A[end] == target:
                return [start, end]
            mid = (start + end) / 2
            if A[mid] < target:
                return helper(mid + 1, end, A)
            elif A[mid] > target:
                return helper(start, mid - 1, A)
            else:
                # ugly codes
                # return [min(helper(start, mid - 1, A)[0], mid), max(mid, helper(mid + 1, end, A)[1])]
                # better
                left = helper(start, mid - 1, A)
                right = helper(mid + 1, end, A)
                return [min(left[0], mid), max(mid, right[1])]
            
            
        if not A:
            return [-1, -1]
            
        length = len(A)
        ans = helper(0, length - 1, A)
        if ans[0] == float('inf'):
            return [-1, -1]
        return ans
        
        