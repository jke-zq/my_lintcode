class ZigzagIterator:

    # @param {int[]} v1 v2 two 1d vectors
    def __init__(self, v1, v2):
        # initialize your data structure here
        self.v1 = v1
        self.v2 = v2
        self.index1 = 0
        self.index2 = 0
        self.len1 = len(self.v1)
        self.len2 = len(self.v2)
        self.first = self.index1 < self.len1


    def next(self):
        # Write your code here
        if self.first:
            val = self.v1[self.index1]
            self.index1 += 1
            if self.index2 < self.len2:
                self.first = not self.first
            return val
        else:
            val = self.v2[self.index2]
            self.index2 += 1
            if self.index1 < self.len1:
                self.first = not self.first
            return val


    def hasNext(self):
        # Write your code here
        return self.index1 < self.len1 or self.index2 < self.len2
        

# Your ZigzagIterator object will be instantiated and called as such:
# solution, result = ZigzagIterator(v1, v2), []
# while solution.hasNext(): result.append(solution.next())
# Output result