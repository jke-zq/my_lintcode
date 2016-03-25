class MinStack(object):

    def __init__(self):
        # do some intialize if necessary
        self.mins = []
        self.data = []

    def push(self, number):
        # write yout code here
        self.data.append(number)
        if not self.mins or self.mins[-1] >= number:
            self.mins.append(number)

    def pop(self):
        # pop and return the top item in stack
        val = self.data.pop()
        if val == self.mins[-1]:
            self.mins.pop()
        return val

    def min(self):
        # return the minimum number in stack
        return self.mins[-1]