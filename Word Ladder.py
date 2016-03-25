class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def ladderLength(self, start, end, dict):
        # write your code here
        
        queue = [start]
        ans = 0
        visited = set(queue)
        ## error....
        dict.add(end)
        while queue:
            # print queue
            ans += 1
            length = len(queue)
            for __ in range(length):
            # for __ in range(len(queue)):
                word = queue.pop(0)
                if word == end:
                    return ans
                lenWord = len(word)
                for i in range(lenWord):
                # for i in range(len(word)):
                    for c in range(26):
                        newWord = word[0:i] + chr(ord('a') + c) + word[i + 1:]
                        # print newWord
                        if newWord in dict and newWord not in visited:
                            queue.append(newWord)
                            visited.add(newWord)
                
            
                
            
            