class AnimalShelter(object):

    def __init__(self):
        # do some intialize if necessary
        self.animals = []
        self.dogIndex = []
        self.catIndex = []
        self.length = 0
        self.start = 0

    """
    @param {string} name
    @param {int} type, 1 if Animal is dog or 0
    @return nothing
    """
    def enqueue(self, name, type):
        # Write yout code here
        self.animals.append((name, type))
        self.length += 1
        if type == 1:
            self.dogIndex.append(self.length - 1)
        else:
            self.catIndex.append(self.length - 1)

    # return a string
    def dequeueAny(self):
        # Write your code here
        while self.animals[0] is None:
            self.animals.pop(0)
            self.start += 1
        name, type = self.animals[0]
        self.animals.pop(0)
        self.start += 1
        if type == 1:
            self.dogIndex.pop(0)
        else:
            self.catIndex.pop(0)
        return name

    # return a string
    def dequeueDog(self):
        # Write your code here
        index = self.dogIndex[0] - self.start
        name, __ = self.animals[index]
        self.animals[index] = None
        self.dogIndex.pop(0)
        return name
        

    # return a string
    def dequeueCat(self):
        # Write your code here
        index = self.catIndex[0] - self.start
        name, __ = self.animals[index]
        self.animals[index] = None
        self.catIndex.pop(0)
        return name