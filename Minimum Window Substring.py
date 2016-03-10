class Solution:
    """
    @param source: A string
    @param target: A string
    @return: A string denote the minimum window
             Return "" if there is no such a string
    """
    def minWindow(self, source, target):
        # write your code here
        
        # targetHash = collections.defaultdict(int)
        # countHash = collections.defaultdict(int)
        # for t in target:
        #     targetHash[t] += 1
        #     countHash[t] += 1
        
        # sourceHash = collections.defaultdict(int)
        # length = len(source)
        # minLen = float('inf')
        # ret = (-1, -1)
        # back = 0
        # for front in range(length):
        #     if source[front] in targetHash:
        #         sourceHash[source[front]] += 1
        #         if countHash and source[front] in countHash:
        #                 countHash[source[front]] -= 1
        #                 if countHash[source[front]] == 0:
        #                     countHash.pop(source[front])
        #         # print countHash
        #         if not countHash:
        #             while back <= front:
        #                 if source[back] not in targetHash:
        #                     back += 1
        #                 elif sourceHash[source[back]] > targetHash[source[back]]:
        #                     sourceHash[source[back]] -= 1
        #                     back += 1
        #                 else:
        #                     break
        #             if minLen > front - back + 1:
        #                 # print front, back
        #                 minLen = front - back + 1
        #                 ret = (back, front)
        ## solution two
        targetHash = collections.defaultdict(int)
        for t in target:
            targetHash[t] += 1
        targetnum = len(target)
        sourcenum = 0
        minLen = float('inf')
        ret = ""
        j = 0
        for i in range(len(source)):
            if targetHash[source[i]] > 0:
                sourcenum += 1
            targetHash[source[i]] -= 1
            while sourcenum >= targetnum:
                targetHash[source[j]] += 1
                if targetHash[source[j]] > 0:
                    sourcenum -= 1
                if minLen > i - j + 1:
                    minLen = i - j + 1
                    ret = source[j:i + 1]
                j += 1
        return ret
                
                
        