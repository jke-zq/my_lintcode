# class Solution:
#     # @param start, a string
#     # @param end, a string
#     # @param dict, a set of string
#     # @return a list of lists of string
#     def findLadders(self, start, end, dict):
#         # write your code here
#         def dfs(word, hashend, tmp, ret):
#             if word == None:
#                 ret.append(tmp[::-1])
#             else:
#                 tmp.append(word)
#                 for w in hashend[word]:
#                     dfs(w, hashend, tmp, ret)
#                 tmp.pop()
        
#         queue = [start]
#         # hashend = collections.defaultdict(list)
#         hashend = collections.defaultdict(set)
#         hashend[start].add(None)
#         dict.add(end)
#         finished = (start == end)
#         while queue:
#             if finished:
#                 break
#             ### error
#             newRoundWords = set()
#             for __ in range(len(queue)):
#                 word = queue.pop(0)
#                 for i in range(len(word)):
#                     for c in range(26):
#                         newWord = word[0:i] + chr(ord('a') + c) + word[i + 1:]
#                         if newWord in dict:
#                             if newWord not in hashend:
#                             # if not hashend[newWord]:
#                                 queue.append(newWord)
#                                 newRoundWords.add(newWord)
#                             if newWord in newRoundWords:
#                                 hashend[newWord].add(word)
#                         if newWord == end:
#                             finished = True
                
        
#         # dfs to find the solution
#         ret, tmp = [], []
#         dfs(end, hashend, tmp, ret)
#         return ret
#                             

class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def findLadders(self, start, end, dict):
        # write your code here
        def bfs(start, end, dict, distances, parents):
            queue = [start]
            distances[start] = 0
            dict.add(end)
            while queue:
                word = queue.pop(0)
                if word == end:
                    return
                nexts = nextWords(word, dict)
                for nw in nexts:
                    if nw not in distances:
                        queue.append(nw)
                        distances[nw] = distances[word] + 1
                    parents[nw].add(word)
                    
        def nextWords(word, dict):
            ans = []
            for i in range(len(word)):
                for c in range(26):
                    nw = word[:i] + chr(c + ord('a')) + word[i + 1:]
                    if nw in dict:
                        ans.append(nw)
            return ans
        
        def dfs(start, tmp, ret, distances, parents):
            if distances[start] == 0:
                ret.append(tmp[::-1])
                return
            for parent in parents[start]:
                if distances[parent] + 1 == distances[start]:
                    tmp.append(parent)
                    dfs(parent, tmp, ret, distances, parents)
                    tmp.pop()
                    
        distances = collections.defaultdict(int)
        parents = collections.defaultdict(set)
        bfs(start, end, dict, distances, parents)
        tmp, ret = [end], []
        dfs(end, tmp, ret, distances, parents)
        return ret
        