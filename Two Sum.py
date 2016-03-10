class Solution:
    """
    @param numbers : An array of Integer
    @param target : target = numbers[index1] + numbers[index2]
    @return : [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here
        
        if not numbers:
            return []
        sortedList = []
        for i, n in enumerate(numbers):
            sortedList.append((n, i))
        sortedList.sort()
        
        length = len(numbers)
        left, right = 0, length - 1
        while left < right:
            total = sortedList[left][0] + sortedList[right][0]
            if total > target:
                right -= 1
            elif total < target:
                left += 1
            else:
                return sorted([sortedList[left][1] + 1, sortedList[right][1] + 1])
                left += 1
                right -= 1