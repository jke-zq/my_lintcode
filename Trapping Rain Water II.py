import heapq


class Solution:
    # @param heights: a matrix of integers
    # @return: an integer
    def trapRainWater(self, heights):
        # write your code here
        # heapq-element:(height, (x, y))

        m, n = len(heights), len(heights[0])
        visited = [[False for __ in range(n)] for __ in range(m)]
        heap = []
        for i in range(m):
            if i == 0 or i == m - 1:
                for j in range(n):
                    heap.append((heights[i][j], (i, j)))
                    visited[i][j] = True
            else:
                heap.append((heights[i][0], (i, 0)))
                visited[i][0] = True
                heap.append((heights[i][n - 1], (i, n - 1)))
                visited[i][n - 1] = True
        heapq.heapify(heap)
        ret = 0
        DICTS = ((-1, 0), (0, 1), (0, -1), (1, 0))
        while heap:
            hei, (x, y) = heapq.heappop(heap)
            for r, c in DICTS:
                nr, nc = x + r, y + c
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                    ret += max(0, hei - heights[nr][nc])
                    ## import to set max(hei, heights[nr][nc])
                    heapq.heappush(heap, (max(hei, heights[nr][nc]), (nr, nc)))
                    visited[nr][nc] = True
            # queue = [(x, y)]
            # while queue:
            #     cx, cy = queue.pop(0)
            #     for r, c in DICTS:
            #         nr, nc = cx + r, cy + c
            #         if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
            #             if heights[nr][nc] > hei:
            #                 heapq.heappush(heap, (heights[nr][nc], (nr, nc)))
            #             else:
            #                 ret += hei - heights[nr][nc]
            #                 queue.append((nr, nc))
            #             visited[nr][nc] = True
        return ret