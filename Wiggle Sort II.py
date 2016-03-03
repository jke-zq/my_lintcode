#         nums[::2], nums[1::2] = nums[med::-1], nums[:med:-1]
import random
class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # nums.sort()
        # med = (len(nums) - 1) / 2
        # nums[::2], nums[1::2] = nums[med::-1], nums[:med:-1]
        def partition(nums, left, right, k):
            A = nums
            left, right = 0, len(A) - 1
            while left <= right:
                pivot = random.randint(left, right)
                #change pivot
                A[right], A[pivot] = A[pivot], A[right]
                newpivot = left
                for i in range(left, right):
                    if A[i] > A[right]:
                        A[newpivot], A[i] = A[i], A[newpivot]
                        newpivot += 1
                        
                A[newpivot], A[right] = A[right], A[newpivot]
                
                if newpivot + 1 == k:
                    return A[newpivot]
                elif newpivot + 1 > k:
                    right = newpivot - 1
                else:
                    left = newpivot + 1
            # return A[left]
        if not nums:
            return nums
        length = len(nums)
        mid = partition(nums, 0, length - 1, (length + 1) / 2)
        tranf = lambda x: (1 + 2 * x) % (length | 1)
        i, j, k = 0, 0, length - 1
        while j <= k:
            if nums[tranf(j)] > mid:
                nums[tranf(i)], nums[tranf(j)] = nums[tranf(j)], nums[tranf(i)]
                i, j = i + 1, j + 1
            elif nums[tranf(j)] < mid:
                nums[tranf(j)], nums[tranf(k)] = nums[tranf(k)], nums[tranf(j)]
                k -= 1
            else:
                j += 1
        
        ##or      
        # ret = [mid for __ in range(length)]
        # l, r = 1, length - 2 if length % 2 == 0 else length - 1
        # for i in range(length):
        #     if nums[i] > mid:
        #         ret[l] = nums[i]
        #         l  += 2
        #     if nums[i] < mid:
        #         ret[r] = nums[i]
        #         r -= 2
        # nums[:] = ret
        