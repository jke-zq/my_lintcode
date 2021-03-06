import random
class Solution:
    # @param k & A a integer and an array
    # @return ans a integer
    def kthLargestElement(self, k, A):
        
        if not A:
            return
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


import random
class Solution:
    # @param k & A a integer and an array
    # @return ans a integer

    def kthLargestElement(self, k, A):
        def swap(index1, index2, A):
            A[index1], A[index2] = A[index2], A[index1]
           
        if not A:
            return None
            
        length = len(A)
        if length < k:
            return None
        
        left, right = 0, length - 1
        while left <= right:
            index = random.randint(left, right)
            swap(index, right, A)
            # target = 
            pivot = left
            for i in range(left, right):
                if A[i] > A[right]:
                    swap(i, pivot, A)
                    pivot += 1
            
            swap(right, pivot, A)
            if pivot + 1 == k:
                return A[pivot]
            elif pivot + 1 < k:
                left = pivot + 1
            else:
                right = pivot - 1
        
        return None



import random
class Solution:
    # @param k & A a integer and an array
    # @return ans a integer
    def kthLargestElement(self, k, A):
        ## [5, 5, 5, 5, 5, 5]
        
        if not A:
            return None
        length = len(A)
        if k > length or k < 1:
            return None
        left, right = 0, length - 1
        while left <= right:
            pivot = random.randint(left, right)
            ## three colors
            ## for testcase: [5, 5, 5, 5, 5, 5] with replication
            target = A[pivot]
            start, end = left, right
            pre = start
            while start <= end:
                if A[start] > target:
                    A[pre], A[start] = A[start], A[pre]
                    pre += 1
                    start += 1
                elif A[start] == target:
                    start += 1
                else:
                    A[end], A[start] = A[start], A[end]
                    end -= 1
            if pre + 1 <= k <= end + 1:
                return A[pre]
            elif pre + 1 > k:
                right = pre - 1
            else:
                left = end + 1
            
            # target = A[pivot]
            # A[right], A[pivot] = A[pivot], A[right]
            # pre = left
            # for i in range(left, right):
            #     if A[i] > target:
            #         A[pre], A[i] = A[i], A[pre]
            #         pre += 1
            # A[right], A[pre] = A[pre], A[right]
            # if pre + 1 == k:
            #     return A[pre]
            # elif pre + 1 > k:
            #     right = pre - 1
            # else:
            #     left = pre + 1
        # raise Exception
        return None