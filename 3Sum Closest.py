class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target : An integer
    @return : return the sum of the three integers, the sum closest target.
    """
    def threeSumClosest(self, numbers, target):
        # write your code here
        numbers.sort()
        length = len(numbers)
        ans = float('inf')
        for i in range(length):
            if i > 0 and numbers[i] == numbers[i - 1]:
                continue
            left, right = i + 1, length - 1
            while left < right:
                diff = target - numbers[i] - numbers[left] - numbers[right] 
                ans = target - diff if abs(diff) < abs(ans - target) else ans
                if diff > 0:
                    left += 1
                elif diff < 0:
                    right -= 1
                else:
                    return target
        return ans