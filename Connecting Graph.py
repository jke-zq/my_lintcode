class ConnectingGraph:

    # @param {int} n
    def __init__(self, n):
        # initialize your data structure here.
        # error:n+1 => n, restrict call
        self.fathers = [0 for _ in range(n + 1)]

    def find(self, x):
        if self.fathers[x] == 0:
            return x
        self.fathers[x] = self.find(self.fathers[x])
        return self.fathers[x]

    # @param {int} a, b
    # return nothing
    def connect(self, a, b):
        # Write your code here
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.fathers[root_a] = root_b

    # @param {int} a, b
    # return {boolean} true if they are connected or false
    def query(self, a, b):
        # Write your code here
        root_a = self.find(a)
        root_b = self.find(b)
        return root_a == root_b
