# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    # @param {int} n an integer
    # @param {int} m an integer
    # @param {Pint[]} operators an array of point
    # @return {int[]} an integer array
    def numIslands2(self, n, m, operators):
        # Write your code here
        
        def compressFind(fathers, x):
            parent = fathers.get(x)
            while parent != fathers.get(parent):
                parent = fathers.get(parent)
            ## parent is the top
            fa = x
            while fa != fathers.get(fa):
                tmp = fathers.get(fa)
                fathers[fa] = parent
                fa = tmp
            return parent
            
        # def union(fathers, x, y, count):
        #     px = compressFind(fathers, x)
        #     py = compressFind(fathers, y)
        #     if px != py:
        #         fathers[px] = py
        #         return count - 1
        #     else:
        #         return count
        def union(fathers, x, y):
            px = compressFind(fathers, x)
            py = compressFind(fathers, y)
            if px != py:
                fathers[px] = py

        matrix = [[0] * m for __ in range(n)]
        fathers = {}
        DICTS = ((-1, 0), (1, 0), (0, -1), (0, 1))
        ret = []
        count = 0
        transfer = lambda x, y: x * m + y
        for p in operators:
            count += 1
            r, c = p.x, p.y
            matrix[r][c] = 1
            x = transfer(r, c)
            fathers[x] = x
            for dx, dy in DICTS:
                nx, ny = dx + r, dy + c
                if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 1:
                    y = transfer(nx, ny)
                    if y not in fathers:
                        fathers[y] = y
                    ## not need to change the union
                    px = compressFind(fathers, x)
                    py = compressFind(fathers, y)
                    if px != py:
                        count -= 1
                        union(fathers, px, py)
                    # count = union(fathers, x, y, count)
            ret.append(count)
        return ret
                        
        
            