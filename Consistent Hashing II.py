import random
class Solution:

    # @param {int} n a positive integer
    # @param {int} k a positive integer
    # @return {Solution} a Solution object
    @classmethod
    def create(cls, n, k):
        # Write your code here
        solution = cls()
        solution.n = n
        solution.k = k
        solution.usedIds = [-1] * solution.n
        solution.unusedIds = range(solution.n)
        return solution


    # @param {int} machine_id an integer
    # @return {int[]} a list of shard ids
    def addMachine(self, machine_id):
        # write your code here
        chosed = random.sample(self.unusedIds, self.k)
        for index in chosed:
            self.unusedIds.remove(index)
            self.usedIds[index] = machine_id
        return chosed
        
        


    # @param {int} hashcode an integer
    # @return {int} a machine id
    def getMachineIdByHashCode(self, hashcode):
        # write your code here
        
        index = hashcode
        while index < self.n:
            if self.usedIds[index] != -1:
                return self.usedIds[index]
            index += 1
        index = 0
        while index < hashcode:
            if self.usedIds[index] != -1:
                return self.usedIds[index]
            index += 1
        return -1
            
            