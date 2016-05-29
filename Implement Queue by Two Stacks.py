class MyQueue:

    def __init__(self):
        self.stack1 = [] #in
        self.stack2 = [] #out
        
    def push(self, element):
        # write your code here
        self.stack1.append(element)
        

    def top(self):
        # write your code here
        # return the top element
        self.__touch()
        return self.stack2[-1]

    def pop(self):
        # write your code here
        # pop and return the top element
        self.__touch()
        return self.stack2.pop()
        
    def __touch(self):
        if self.stack2:
            return
        while self.stack1:
            self.stack2.append(self.stack1.pop())