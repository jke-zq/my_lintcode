class Solution:
    # @param {int[][]} costs n x k cost matrix
    # @return {int} an integer, the minimum cost to paint all houses
    def minCostII(self, costs):
        # Write your code here
        ## maximum recursion depth exceeded while calling a Python object
        # def helper(visited, n, k, results, costs):
        #     if n == 0:
        #         return 0
        #     if results[n - 1][visited] > 0:
        #         return results[n - 1][visited]
        #     val = float('inf')
        #     for i in range(k):
        #         if i == visited:
        #             continue
        #         val = min(val, costs[n - 1][i] + helper(i, n - 1, k, results, costs))
        #     results[n - 1][visited] = val
        #     return results[n - 1][visited]

        # if len(costs) == 0:
        #     return 0
        # n, k = len(costs), len(costs[0])
        # results = [[-1] * k for __ in range(n)]
        # return helper(-1, n, k, results, costs)

        # Time Limit Exceeded
        # O(nkk) to O(nk)
        if len(costs) == 0:
            return 0
        n, k = len(costs), len(costs[0])
        results = [[0] * k for __ in range(n)]
        min_1, min_2 = float('inf'), float('inf')
        for i in range(k):
            results[0][i] = costs[0][i]
            if min_1 < costs[0][i]:
                min_2 = min(min_2, costs[0][i])
            else:
                min_2, min_1 = min_1, costs[0][i]

        for i in range(1, n):
            new_min_1, new_min_2 = float('inf'), float('inf')
            for j in range(k):
                if results[i - 1][j] == min_1:
                    results[i][j] = costs[i][j] + min_2
                else:
                    results[i][j] = costs[i][j] + min_1
                if new_min_1 < results[i][j]:
                    new_min_2 = min(new_min_2, results[i][j])
                else:
                    new_min_2, new_min_1 = new_min_1, results[i][j]
            min_1, min_2 = new_min_1, new_min_2
        return min(results[-1])

