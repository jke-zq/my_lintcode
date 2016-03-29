## TLE
# class WebLogger:
    
#     def __init__(self):
#         # initialize your data structure here.
#         self.hitDict = collections.defaultdict(int)
#         self.currentTime = None
#         self.currentAns = 0


#     # @param {int} timestamp an integer
#     # @return nothing
#     def hit(self, timestamp):
#         # Write your code here
#         self.hitDict[timestamp] += 1
#         if self.currentTime and self.currentTime == timestamp:
#             self.currentAns += 1
#         else:
#             self.currentTime = None


#     # @param {int} timestamp an integer
#     # @return {int} an integer
#     def get_hit_count_in_last_5_minutes(self, timestamp):
#         # Write your code here
#         if timestamp == self.currentTime:
#             return self.currentAns
        
#         ans = 0
#         for key in range(timestamp - 299, timestamp + 1):
#             ans += self.hitDict.get(key, 0)
#         if self.currentTime is None:
#             self.currentTime = timestamp
#             self.currentAns = ans
#         return ans
            
class WebLogger:
    
    def __init__(self):
        # initialize your data structure here.
        self.data = []
        self.dataLen = 0
        self.hits = 0


    # @param {int} timestamp an integer
    # @return nothing
    def hit(self, timestamp):
        # Write your code here
        if self.dataLen > 0 and self.data[-1][0] == timestamp:
            self.data[-1][1] += 1
        else:
            self.data.append([timestamp, 1])
            self.dataLen += 1
        self.hits += 1

    # @param {int} timestamp an integer
    # @return {int} an integer
    def get_hit_count_in_last_5_minutes(self, timestamp):
        # Write your code here
        while self.dataLen > 0 and self.data[0][0] < timestamp - 299:
            self.hits -= self.data[0][1]
            self.data.pop(0)
            self.dataLen -= 1
        return self.hits
