class Solution:
    """
    @param a, b, n: 32bit integers
    @return: An integer
    """
    def fastPower(self, a, b, n):
        # write your code here
        if a > b:
            return self.fastPower(a % b, b, n)
        
        if n == 0:
            return 1 % b
            
        if n % 2 == 1:
            return (a * self.fastPower(a, b, n - 1)) % b
        else:
            # val = self.fastPower(a, b, n / 2)
            # return ((val % b) ** 2) % b
            return self.fastPower((a * a) % b, b, n / 2) % b