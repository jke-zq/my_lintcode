class RateLimiter:

    def __init__(self):
        # do some intialize if necessary
        self.data = collections.defaultdict(list)
        self.hits = collections.defaultdict(int)
        self.carrys = {'h': 3600, 'd': 24 * 3600, 'm': 60, 's': 1}
        
    def __increment(self, timestamp, event):
        data = self.data[event]
        if len(data) > 0 and data[-1][0] == timestamp:
            data[-1][1] += 1
        else:
            data.append([timestamp, 1])
        # self.hits[event] += 1
    
    def __lessThanLimited(self, timestamp, event, rate):
        data = self.data[event]
        limited, kind = rate.split('/')
        limited, carry = int(limited), self.carrys[kind]
        total = 0
        for i in data[::-1]:
            if i[0] > timestamp - carry:
                total += i[1]
            # data.pop()
        return limited - total
        
        
    # @param {int} timestamp the current timestamp
    # @param {string} event the string to distinct different event
    # @param {string} rate the format is [integer]/[s/m/h/d]
    # @param {boolean} increment whether we should increase the counter
    # @return {boolean} true of false to indicate the event is limited or not
    def is_ratelimited(self, timestamp, event, rate, increment):
        # Write your code here
        left = self.__lessThanLimited(timestamp, event, rate)
        if left <= 0:
            return False
            
        if increment:
            self.__increment(timestamp, event)
        return True