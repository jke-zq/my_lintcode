# Definition for a directed graph node
# class DirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []
class Solution:
    # @param {DirectedGraphNode[]} nodes a array of directed graph node
    # @return {int[][]} a connected set of a directed graph
    def connectedSet2(self, nodes):
        # Write your code here
        def compressFind(fathers, x):
            parent = fathers.get(x)
            while parent != fathers.get(parent):
                parent = fathers.get(parent)
            # parent is the top
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
                
        if not nodes:
            return []
        fathers = {}
        for node in nodes:
            fathers[node.label] = node.label
        for node in nodes:
            for nei in node.neighbors:
                union(fathers, node.label, nei.label)
        # compress the path
        for key in nodes:
            compressFind(fathers, key.label)
        ret = collections.defaultdict(list)
        for k, v in fathers.items():
            ret[v].append(k)
        
        return [sorted(v) for v in ret.values()]
        