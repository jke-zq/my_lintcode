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
            # if g not in dicts:
            #     dicts[g] = 0
            for gnb in g.neighbors:
                dicts[gnb] += 1
        
        ## init the queue to BFS
        queue = []
        for g in graph:
            if dicts[g] == 0:   ## if g not in dicts, values will be int() default value
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
                

##solution two

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
        dicts = collections.defaultdict(int) # node:indegree
        for g in graph:
            dicts[g] += 0      ## needed for the dicts.keys()
            for gnb in g.neighbors:
                dicts[gnb] += 1
        
        ans = []
        for g in dicts.keys():
            if dicts[g] == 0:
                ans.append(g)
        length = len(ans)
        start = 0
        while start < length:
            g = ans[start]
            for nb in g.neighbors:
                dicts[nb] -= 1
                if dicts[nb] == 0:
                    ans.append(nb)
                    length += 1
            start += 1
                    
        return ans
                

                