class Solution:
    # @param {int[][]} arrays k sorted integer arrays
    # @return {int[]} a sorted array
    def mergekSortedArrays(self, arrays):
        # Write your code here
        ## 3 solution
        def merge(list1, list2):
            if not list1:
                return list2
            if not list2:
                return list1
            len1, len2 = len(list1), len(list2)
            start1, start2 = 0, 0
            ans = []
            while start1 < len1 and start2 < len2:
                if list1[start1] > list2[start2]:
                    ans.append(list2[start2])
                    start2 += 1
                else:
                    ans.append(list1[start1])
                    start1 += 1
                    
            if start1 < len1:
                ans.extend(list1[start1:])
            if start2 < len2:
                ans.extend(list2[start2:])
            return ans
            
            
        if not arrays:
            return []
        length = len(arrays)
        while length > 1:
            left, right = 0, length - 1
            nextArray = []
            while left < right:
                nextArray.append(merge(arrays[left], arrays[right]))
                left, right = left + 1, right - 1
                
            if left == right:
                nextArray.append(arrays[left])
            length = len(nextArray)
            arrays = nextArray
        return arrays[0]