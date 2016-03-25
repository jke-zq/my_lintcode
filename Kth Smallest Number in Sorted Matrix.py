import heapq
class Solution:
    # @param matrix: a matrix of integers
    # @param k: an integer
    # @return: the kth smallest number in the matrix
    def kthSmallest(self, matrix, k):
        # write your code here
        
        if not matrix or not matrix[0]:
            return None
        length = len(matrix)
        heap = []
        for i in range(length):
            heapq.heappush(heap, (matrix[i][0], i, 0))
        COLS = len(matrix[0])
        for i in range(k - 1):
            __, row, col = heapq.heappop(heap)
            if col < COLS - 1:
                heapq.heappush(heap, (matrix[row][col + 1], row, col + 1))
        return heapq.heappop(heap)[0]