class Solution:
    # @param {int} n an integer
    # @param {int[][]} edges a list of undirected edges
    # @return {boolean} true if it's a valid tree, or false
    def validTree(self, n, edges):
        # Write your code here
        
        def compressFind(fathers, x):
            parent = fathers.get(x)
            while parent != fathers.get(parent):
                parent = fathers.get(parent)
            
            #parent is the top
            fa = x
            while fa != fathers.get(fa):
                tmp = fathers.get(fa)
                fathers[fa] = parent
                fa = tmp
            return parent
        
        def union(fathers, x, y):
            px = compressFind(fathers, x)
            py = compressFind(fathers, y)
            if px != py:
                fathers[px] = py
        ## error: there should be n - 1 edges
        if n - 1 != len(edges):
            return False
        # if n == 1:
        #     return True
        # if not edges:
        #     return False
        fathers = {}
        for i in range(n):
            fathers[i] = i
        for edge in edges:
            x, y = edge
            px = compressFind(fathers, x)
            py = compressFind(fathers, y)
            if px != py:
                union(fathers, px, py)
            else:
                return False
        
        # roots = set()
        # for k in fathers:
        #     roots.add(compressFind(fathers, k))
        #     if len(roots) > 1:
        #         return False
        return True