class Solution:
    # @param {string} str a string
    # @return {string[]} all permutations
    def stringPermutation2(self, str):
        # Write your code here
        
        def helper(left, visited, tmp, ret, str, length):
            if left == 0:
                ret.append(tmp)
                return
            # else:
            for index in range(length):
                if visited[index]:
                    continue
                if index > 0 and str[index] == str[index - 1] and not visited[index - 1]:
                    continue
                # tmp.append(str[index])
                visited[index] = True
                helper(left - 1, visited, tmp + str[index], ret, str, length)
                visited[index] = False
                # tmp.pop()
        # if not str:
        #     return []
        length = len(str)
        ## error
        # str.sort()
        str = sorted(str)
        visited = [False] * length
        tmp, ret = "", []
        helper(length, visited, "", ret, str, length)
        return ret
                        