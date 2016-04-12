class Solution:
    """
    @param numbersbers : Give an array numbersbers of n integer
    @return : Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        # write your code here
        if not numbers:
            return []
        numbers.sort()
        ans = []
        
        length = len(numbers)
        for i in range(length):
            if i > 0 and numbers[i] == numbers[i - 1]:
                continue
            left, right = i + 1, length - 1
            while left < right:
                total = numbers[i] + numbers[left] + numbers[right]
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    ans.append([numbers[i], numbers[left], numbers[right]])
                    left += 1
                    while left < right and numbers[left] == numbers[left - 1]:
                        left += 1
                    right -= 1
                    while left < right and numbers[right] == numbers[right + 1]:
                        right -= 1
        return ans