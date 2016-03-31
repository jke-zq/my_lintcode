class Solution:
    """
    @param A: An integer array.
    @param k: A positive integer (k <= length(A))
    @param target: Integer
    @return a list of lists of integer 
    """
    def kSumII(self, A, k, target):
        # # write your code here
        def helper(start, k, total, tmp, ret, length, A, target):
            if k == 0:
                if total == target:
                    ret.append(tmp[:])
                return
            ## add this reduce the runtime
            if total >= target:
                return
            for i in range(start, length):
                tmp.append(A[i])
                helper(i + 1, k - 1, total + A[i], tmp, ret, length, A, target)
                tmp.pop()
                
        if not A:
            return []
        A.sort()
        tmp, ret = [], []
        length = len(A)
        helper(0, k, 0, tmp, ret, length, A, target)
        return ret
        
        # def dfs(A, k, target, index, onelist):
            
        #     if(target == 0 and k == 0):
        #         self.anslist.append(onelist)
        #         return None
        #     if(len(A) == index or target < 0 or k < 0):
        #         return None
        #     dfs(A, k, target, index + 1, onelist)
        #     otheronelist = [A[index]]
        #     otheronelist.extend(onelist)
        #     dfs(A, k - 1, target - A[index],  index + 1 , otheronelist)

        # self.anslist = []
        # dfs(A, k, target, 0, [])
        # return self.anslist