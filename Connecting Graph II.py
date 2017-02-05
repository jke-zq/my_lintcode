class ConnectingGraph2:

    # @param {int} n
    def __init__(self, n):
        # initialize your data structure here.
        self.father = [0] * (n + 1)
        self.size = [1] * (n + 1)

    def find(self, x):
        if self.father[x] == 0:
            return x
        self.father[x] = self.find(self.father[x])
        return self.father[x]

    # @param {int} a, b
    # return nothing
    def connect(self, a, b):
        # Write your code here
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.father[root_a] = root_b
            self.size[root_b] += self.size[root_a]

    # @param {int} a
    # return {int}  the number of nodes connected component
    # which include a node.
    def query(self, a):
        # Write your code here
        root_a = self.find(a)
        return self.size[root_a]
