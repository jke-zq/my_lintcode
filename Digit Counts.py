class Solution:
    # @param k & n  two integer
    # @return ans a integer
    def digitCounts(self, k, n):
        
        ans = 0
        for i in range(n + 1):
            # if i == k:
            #     ans += 1
            #     i /= 10
            # while i:
            #     if i % 10 == k:
            #         ans += 1
            #     i /= 10
            ## j == i
            while True:
                if i % 10 == k:
                    ans += 1
                i /= 10
                if i == 0:
                    break
        return ans