# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []
class Solution:
    # @param {UndirectedGraphNode[]} nodes a array of undirected graph node
    # @return {int[][]} a connected set of a undirected graph
    def connectedSet(self, nodes):
        # Write your code here
        def bfs(node, visited, ret):
            tmp = []
            queue = [node]
            while queue:
                p = queue.pop(0)
                if p not in visited:
                    tmp.append(p.label)
                    visited.add(p)
                    for child in p.neighbors:
                        queue.append(child)
            ## error: change the final result in the func
            tmp.sort()
            ret.append(tmp)

        def dfs(node, visited, tmp):
            visited.add(node)
            tmp.append(node.label)
            for child in node.neighbors:
                if child not in visited:
                    dfs(child, visited, tmp)
            
        if not nodes:
            return []
        visited = set()
        ## dfs
        # ret, tmp = [], []
        # for node in nodes:
        #     if node not in visited:
        #         if tmp:
        #             tmp.sort()
        #             ret.append(tmp)
        #         tmp = []
        #         dfs(node, visited, tmp)
        # tmp.sort()
        # ret.append(tmp)
        ## bfs
        ret = []
        for node in nodes:
            if node not in visited:
                bfs(node, visited, ret)
        return ret
        
        # def compressFind(fathers, x):
        #     parent = fathers.get(x)
        #     while parent != fathers.get(parent):
        #         parent = fathers.get(parent)
        #     #parent is the topest node
        #     tmp = None
        #     # error
        #     # fa = fathers.get(x)
        #     fa = x
        #     while fa != fathers.get(fa):
        #         tmp = fathers.get(fa)
        #         fathers[fa] = parent
        #         fa = tmp
        #     return parent
            
        # def union(fathers, x, y):
        #     px = compressFind(fathers, x)
        #     py = compressFind(fathers, y)
        #     if px != py:
        #         fathers[px] = py
        
        # if not nodes:
        #     return []
        # fathers = {}
        # for node in nodes:
        #     fathers[node.label] = node.label
        
        # for node in nodes:
        #     for child in node.neighbors:
        #         union(fathers, child.label, node.label)
        # ## important:--clean up the top
        # for k in fathers:
        #     compressFind(fathers, k)
        # #find the result
        # ret = collections.defaultdict(list)
        # for k, v in fathers.items():
        #     ret[v].append(k)
        # return [sorted(v) for v in ret.values()]
            
## using BFS
## comment with whitespace
## using list.sort(), but its return value is None
## if BFS is a func, then change the final result in the func

            