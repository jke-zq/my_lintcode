class Solution:
    """
    @param A: An integer array.
    @param k: a positive integer (k <= length(A))
    @param target: integer
    @return an integer
    """
    def kSum(self, A, k, target):
        # write your code here
        
        d = [[[0] * (target + 1) for __ in range(1 + k)] for __ in range(2)]
        d[0][0][0] = 1

        for i in range(1, len(A) + 1):
            d[i % 2][0][0] = 1
            for j in range(1, k + 1):
                for t in range(1, target + 1):
                    d[i % 2][j][t] = d[(i - 1) % 2][j][t]
                    if A[i - 1] <= t:
                        d[i % 2][j][t] += d[(i - 1) % 2][j - 1][t - A[i - 1]]
        return d[len(A) % 2][k][target]