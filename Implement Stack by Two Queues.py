class Stack:
    # initialize your data structure here.
    def __init__(self):
        self.inq = []

    # @param x, an integer, push a new item into the stack
    # @return nothing
    def push(self, x):
        # Write your code here
        self.inq.append(x)

    # @return nothing, pop the top of the stack
    def pop(self):
        # Write your code here
        self.__exchange()
        return self.inq.pop(0)

    # @return an integer, return the top of the stack
    def top(self):
        # Write your code here
        top = self.pop()
        self.push(top)
        return top
        
    # @return an boolean, check the stack is empty or not.
    def isEmpty(self):
        # Write your code here
        return self.inq == []
    
    def __exchange(self):
        length = len(self.inq)
        for __ in range(length - 1):
            self.inq.append(self.inq.pop(0))
            