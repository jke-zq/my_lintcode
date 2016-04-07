'''
Definition of Document
class Document:
    def __init__(self, id, cotent):
        self.id = id
        self.content = content
'''
class Solution:
    # @param {Document[]} docs a list of documents
    # @return {dict(string, int[])} an inverted index
    def invertedIndex(self, docs):
        # Write your code here
        ans = collections.defaultdict(set)
        for doc in docs:
            for w in doc.content.split():
                ans[w].add(doc.id)
        for k, v in ans.items():
            ans[k] = sorted(list(v))
        return ans
            
                
