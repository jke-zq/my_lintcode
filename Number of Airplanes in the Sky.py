"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    # @param airplanes, a list of Interval
    # @return an integer
    def countOfAirplanes(self, airplanes):
        # write your code here
        airs = []
        for interval in airplanes:
            s, e = interval.start, interval.end
            airs.append((s, 1))
            airs.append((e, 0))
        
        airs.sort()
        count = 0
        ret = 0
        for time, fly in airs:
            if fly == 1:
                count += 1
                ret = max(ret, count)
            else:
                count -= 1
            
        return ret