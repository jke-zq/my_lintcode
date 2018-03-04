class Solution:
    """
    @param dividend: the dividend
    @param divisor: the divisor
    @return: the result
    """
    def divide(self, dividend, divisor):
        # write your code here
        if divisor == 0:
            return 2147483647

        dvd, dvs = abs(dividend), abs(divisor)
        mult = dvs
        times = 1
        while mult <= dvd:
            mult <<= 1
            times <<= 1
        ret = 0
        while dvd >= dvs:
            while mult > dvd:
                mult >>= 1
                times >>= 1
            dvd -= mult
            ret += times

        if (dividend > 0) ^ (divisor > 0):
            return 0 - ret
        else:
            return min(ret, 2147483647)



