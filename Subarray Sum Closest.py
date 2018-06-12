class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number
             and the index of the last number
    """
    def subarraySumClosest(self, nums):
        # write your code here
        # if not nums:
        #     return []
        # length = len(nums)
        # ret = [None] * length
        # ret[0] = (nums[0], 0)
        # for i in range(1, length):
        #     ret[i] = (nums[i] + ret[i - 1][0], i)
        # # sorted(ret)
        # ret.sort()
        # distance = float('inf')
        # ans = []
        # for i in range(1, length):
        #     if distance > abs(ret[i][0] - ret[i - 1][0]):
        #         distance = ret[i][0] - ret[i - 1][0]
        #         ans = [ret[i][1], ret[i - 1][1]]
        # if ans:
        #     ans.sort()
        #     ans[0] += 1
        #     return ans
        # else:
        #     return [0, 0]

        length = len(nums)
        pre_sums = [None] * (length + 1)
        pre_sums[0] = (0, 0)
        for i, n in enumerate(nums):
            pre_sums[i + 1] = (pre_sums[i][0] + n, i + 1)

        pre_sums.sort(key=lambda x: x[0])
        ans = []
        closest = float('inf')
        for i in range(1, length + 1):
            tmp = abs(pre_sums[i][0] - pre_sums[i - 1][0])
            if closest > tmp:
                closest = tmp
                if pre_sums[i][1] > pre_sums[i - 1][1]:
                    ans = [[pre_sums[i - 1][1], pre_sums[i][1] - 1]]
                else:
                    ans = [[pre_sums[i][1], pre_sums[i - 1][1] - 1]]

            elif closest == tmp:
                if pre_sums[i][1] > pre_sums[i - 1][1]:
                    ans.append([pre_sums[i - 1][1], pre_sums[i][1] - 1])
                else:
                    ans.append([pre_sums[i][1], pre_sums[i - 1][1] - 1])

        ans.sort()
        # print(ans[-1])
        return ans[-1]
        # return ans
