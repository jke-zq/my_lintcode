class Solution:
    """
    @param numbersbers : Give an array numbersbersbers of n integer
    @param target : you need to find four elements that's sum of target
    @return : Find all unique quadruplets in the array which gives the sum of 
              zero.
    """
    def fourSum(self ,numbers, target):
        # write your code here
        if not numbers:
            return []
        # numbers.sort()
        # length = len(numbers)
        # ans = []
        # for i in range(length - 3):
        #     if i > 0 and numbers[i] == numbers[i - 1]:
        #         continue
        #     for j in range(i + 1, length - 2):
        #         if j > i + 1 and numbers[j] == numbers[j - 1]:
        #             continue
        #         left, right = j + 1, length - 1
        #         while left < right:
        #             total = numbers[i] + numbers[j] + numbers[left] + numbers[right]
        #             if total > target:
        #                 right -= 1
        #                 # while left < right and numbers[right] == numbers[right + 1]:
        #                 #     right -= 1
        #             elif total < target:
        #                 left += 1
        #                 # while left < right and numbers[left] == numbers[left - 1]:
        #                 #     left += 1
        #             else:
        #                 ans.append([numbers[i], numbers[j], numbers[left], numbers[right]])
        #                 left += 1
        #                 right -= 1
        #                 while left < right and numbers[left] == numbers[left - 1]:
        #                     left += 1
        #                 while left < right and numbers[right] == numbers[right + 1]:
        #                     right -= 1
        # return ans
        numbers.sort()
        length = len(numbers)
        hashVal = collections.defaultdict(set)
        for i in range(length):
            for j in range(i + 1, length):
                hashVal[numbers[i] + numbers[j]].add((i, j))
        ans = set()
        for i in range(length):
            if i > 0 and numbers[i] == numbers[i - 1]:
                continue
            for j in range(i + 1, length):
                if j > i + 1 and numbers[j] == numbers[j - 1]:
                    continue
                total = numbers[i] + numbers[j]
                if target - total in hashVal:
                    indexs = hashVal[target - total]
                    for index in indexs:
                        if j < index[0]:
                            ans.add((numbers[i], numbers[j], numbers[index[0]], numbers[index[1]]))
        return [list(v) for v in ans]
                
                
