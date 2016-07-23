# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return {boolean} True if this NestedInteger holds a single integer,
#        rather than a nested list.
#        """
#
#    def getInteger(self):
#        """
#        @return {int} the single integer that this NestedInteger holds,
#        if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self):
#        """
#        @return {NestedInteger[]} the nested list that this NestedInteger holds,
#        if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        # Initialize your data structure here.
        self.indexes = [[0, len(nestedList), nestedList]]

    # @return {int} the next element in the iteration
    def next(self):
        # Write your code here
        index = self.indexes[-1][0]
        self.indexes[-1][0] += 1
        return self.indexes[-1][2][index].getInteger()
    # @return {boolean} true if the iteration has more element or false
    def hasNext(self):
        # Write your code here
        while self.indexes:
            if self.indexes[-1][1] <= self.indexes[-1][0]:
                self.indexes.pop()
                if self.indexes:
                    self.indexes[-1][0] += 1
            else:
                index = self.indexes[-1][0]
                next_v = self.indexes[-1][2][index]
                while not next_v.isInteger():
                    self.indexes.append([0, len(next_v.getList()), next_v.getList()])
                    if not self.indexes[-1][2]:
                        next_v = None
                        break
                    next_v = self.indexes[-1][2][0]
                if next_v is not None:
                    return True
        return False


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
