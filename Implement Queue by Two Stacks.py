class MyQueue:

    def __init__(self):
        self.stack1 = []# input
        self.stack2 = []# output
        
    def push(self, element):
        # write your code here
        self.stack1.append(element)

    def top(self):
        # write your code here
        # return the top element
        self._exchange()
        return self.stack2[-1]

    def pop(self):
        # write your code here
        # pop and return the top element
        self._exchange()
        return self.stack2.pop()
    
    def _exchange(self):
        if not self.stack2:
            self.stack2 = self.stack1[::-1]
            self.stack1 = []
