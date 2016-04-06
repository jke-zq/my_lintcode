'''
Definition of Document
class Document:
    def __init__(self, id, cotent):
        self.id = id
        self.content = content
'''
class InvertedIndex:

    # @param {Document} value is a document
    def mapper(self, _, value):
        # Write your code here
        # Please use 'yield key, value' here
        # key = value.id
        # words = value.content.split()
        # for w in words:
        #     yield w, key
        for word in value.content.split():
            yield word, value.id
        


    # @param key is from mapper
    # @param values is a set of value with the same key
    def reducer(self, key, values):
        # Write your code here
        # Please use 'yield key, value' here
        # ans = set()
        # for v in values:
        #     ans.add(v)
        # # ans.extend(values)
        # yield key, list(ans)
        a = sorted(list(set(values)))
        yield key, a