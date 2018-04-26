# class Solution:
#     """
#     @param nums: A list of integers.
#     @return: A list of unique permutations.
#     """
#     def permuteUnique(self, nums):
#         # write your code here
#         def helper(left, visited, tmp, ret, length):
#             if left == 0:
#                 ret.append(tmp[::])
#             else:
#                 for i in range(length):
#                     if visited[i]:
#                         continue
#                     if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
#                         continue
#                     else:
#                         tmp.append(nums[i])
#                         visited[i] = True
#                         helper(left - 1, visited, tmp, ret, length)
#                         visited[i] = False
#                         tmp.pop()
#         if not nums:
#             return []
#         nums.sort()
#         length = len(nums)
#         visited = [False] * length
#         tmp, ret = [], []
#         helper(length, visited, tmp, ret, length)
#         return ret

class Solution:
    """
    @param: :  A list of integers
    @return: A list of unique permutations
    """

    def permuteUnique(self, nums):
        # write your code here


        def helper(ans, tmp, visited, start, length, nums):
            if start == length:
                ans.append(tmp[:])
                return
            last = None
            for i in range(0, length):
                if visited[i]:
                    continue
                if nums[i] == last:
                    continue
                # if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                    # continue
                last = nums[i]
                visited[i] = True
                tmp.append(nums[i])
                helper(ans, tmp, visited, start + 1, length, nums)
                tmp.pop()
                visited[i] = False

        nums.sort()
        length = len(nums)
        visited = [False] * length
        ans = []
        helper(ans, [], visited, 0, length, nums)
        return ans
