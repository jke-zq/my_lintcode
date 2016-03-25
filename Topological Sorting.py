# Definition for a Directed graph node
# class DirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    """
    @param graph: A list of Directed graph node
    @return: A list of integer
    """
    def topSort(self, graph):
        # write your code here
        if not graph:
            return []
        ## class: graph, count
        ## DFS to mark count
        ## 0(n) to find the count == 0 graph, and BFS from it.
        if not graph:
            return None
        dicts = collections.defaultdict(int) # node:indegree
        for g in graph:
            if g not in dicts:
                dicts[g] = 0
            for gnb in g.neighbors:
                dicts[gnb] += 1
        
        ## init the queue to BFS
        queue = []
        for g in graph:
            if dicts[g] == 0:
                queue.append(g)
        ans = []
        while queue:
            node = queue.pop(0)
            ans.append(node)
            for nb in node.neighbors:
                dicts[nb] -= 1
                if dicts[nb] == 0:
                    queue.append(nb)
        return ans
                
                