class Solution:
    # @param {string[]} words a list of string
    # @param {int} k an integer
    # @return {string[]} a list of string
    def topKFrequentWords(self, words, k):
        # Write your code here
        
        if not words:
            return []
        dicts = collections.defaultdict(int)
        for w in words:
            dicts[w] += 1
        freq = [(v, key) for key, v in dicts.items()]
        fun = lambda x, y: cmp(y[0], x[0]) if x[0] != y[0] else cmp(x[1], y[1])
        freq.sort(cmp = fun)
        return [s[1] for s in freq[:k]]