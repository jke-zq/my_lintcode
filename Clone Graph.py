# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def __init__(self):
        self.dict = {}
        
    def cloneGraph(self, node):
        # write your code here
        # if not node:
        #     return None
        # queue = [node]
        # visited = set()
        # while queue:
        #     n = queue.pop(0)
        #     if n in visited:
        #         continue
        #     else:
        #         visited.add(n)
        #     if n not in self.dict:
        #         cpn = UndirectedGraphNode(n.label)
        #         self.dict[n] = cpn
        #     cpn = self.dict[n]
        #     for nb in n.neighbors:
        #         if nb not in self.dict:
        #             cpnb = UndirectedGraphNode(nb.label)
        #             self.dict[nb] = cpnb
        #         queue.append(nb)
        #         cpn.neighbors.append(self.dict[nb])
        # return self.dict[node]
        
        ## copy node
        if not node:
            return None
        queue = [node]
        while queue:
            n = queue.pop(0)
            ## version 1
            if n not in self.dict:
                self.dict[n] = UndirectedGraphNode(n.label)
                for nb in n.neighbors:
                    queue.append(nb)
            ## version 2
            # if n in self.dict:
            #     continue
            # self.dict[n] = UndirectedGraphNode(n.label)
            # for nb in n.neighbors:
            #     queue.append(nb)
        
        ## assign neighbors
        for n in self.dict.keys():
            cpn = self.dict[n]
            for nb in n.neighbors:
                cpn.neighbors.append(self.dict[nb])
        return self.dict[node]
        
        