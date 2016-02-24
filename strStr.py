class Solution:
    def strStr(self, source, target):
        # write your code here
        
        if source is None or target is None:
            return -1
        else:
            ##error
            # if target == '':
            #     return 0
            len_src, len_tgt = len(source), len(target)
            ##error
            for i in range(len_src - len_tgt + 1):
                j = 0
                while j < len_tgt:
                    if source[j + i] != target[j]:
                        break
                    j += 1
                if j == len_tgt:
                    return i
            return -1