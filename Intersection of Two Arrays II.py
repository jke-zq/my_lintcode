import collections


class Solution:
    # @param {int[]} nums1 an integer array
    # @param {int[]} nums2 an integer array
    # @return {int[]} an integer array
    def intersection(self, nums1, nums2):
        # Write your code here
        # return list(set(nums1) & set(nums2))
        # 1.What if the given array is already sorted? How would you optimize your algorithm?
        # 2.What if nums1's size is small compared to num2's size? Which algorithm is better?
        # 3.What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
        # nums1.sort()
        # nums2.sort()
        # ans = []
        # len1, len2 = len(nums1), len(nums2)
        # left, right = 0, 0
        # while left < len1 and right < len2:
        #     if nums1[left] == nums2[right]:
        #         ans.append(nums1[left])
        #         left += 1
        #         right += 1
        #     elif nums1[left] > nums2[right]:
        #         right += 1
        #     else:
        #         left += 1
        # return ans

        # MLE
        hash1 = collections.defaultdict(int)
        hash2 = collections.defaultdict(int)
        for n in nums1:
            hash1[n] += 1
        for n in nums2:
            hash2[n] += 1
        for k in hash1.keys():
            hash2[k] = -1 * min(hash1[k], hash2[k])
        ans = []
        for k, v in hash2.iteritems():
            for __ in range(-1 * v):
                ans.append(k)
        return ans
