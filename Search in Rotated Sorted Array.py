class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : an integer
    """
    def search(self, A, target):
        # write your code here

        if not A:
            return -1
        left, right = 0, len(A) - 1
        while left + 1 < right:
            mid = left + (right - left) / 2
            if A[mid] == target:
                return mid
            elif target >= A[left]:
                if target > A[mid] > A[left]:
                    left = mid
                else:
                    right = mid
            elif target <= A[right]:
                if A[right] > A[mid] > target:
                    right = mid
                else:
                    left = mid

        if A[left] == target:
            return left
        if A[right] == target:
            return right
        return -1

    # solution II
    def search(self, A, target):
        # write your code here

        if A is None or len(A) == 0:
            return False
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] == target:
                return True
            if A[mid] == A[end]:
                end -= 1
                continue

            if A[mid] < A[end]:
                if A[mid] < target <= A[end]:
                    start = mid
                else:
                    end = mid
            else:
                if A[mid] > target >= A[start]:
                    end = mid
                else:
                    start = mid

        return target in (A[start], A[end])
