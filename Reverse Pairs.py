class Solution:
    # @param {int[]} A an array
    # @return {int} total of reverse pairs
    def reversePairs(self, A):
        # Write your code here
        def dc(start, end, indexes, ans, A):
            if start >= end:
                return
            mid = (start + end) / 2
            dc(start, mid, indexes, ans, A)
            dc(mid + 1, end, indexes, ans, A)
            tmp = []
            j = mid + 1
            for i in range(start, mid + 1):
                while j <= end and A[indexes[j]] < A[indexes[i]]:
                    tmp.append(indexes[j])
                    j += 1
                ans[indexes[i]] += j - mid - 1
                tmp.append(indexes[i])
            indexes[start:len(tmp) + start] = tmp
            
        if not A:
            return 0
        length = len(A)
        indexes = range(length)
        ans = [0] * length
        dc(0, length - 1, indexes, ans, A)
        return sum(ans)
                  