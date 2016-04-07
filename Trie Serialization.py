"""
Definition of TrieNode:
class TrieNode:
    def __init__(self):
        # <key, value>: <Character, TrieNode>
        self.children = collections.OrderedDict()
"""
class Solution:

    '''
    @param root: An object of TrieNode, denote the root of the trie.
    This method will be invoked first, you should design your own algorithm 
    to serialize a trie which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    '''
    def serialize(self, root):
        # Write your code here
        ans = ""
        for k, v in root.children.items():
            ans += k + self.serialize(v)
        return '<' + ans + '>'
            


    '''
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    '''
    def deserialize(self, data):
        # Write your code here
        # def helper(node, data, start, end):
        #     if start + 1 >= end:
        #         return
        #     start += 1
        #     index = start
        #     while index < end:
        #         newEnd = index + 2
        #         count = 1
        #         while newEnd < end and count != 0:
        #             if data[newEnd] == '<':
        #                 count += 1
        #             elif data[newEnd] == '>':
        #                 count -= 1
        #             newEnd += 1
        #         newEnd -= 1
        #         if newEnd > index + 1:
        #             node.children[data[index]] = TrieNode()
        #             helper(node.children[data[index]], data, index + 1, newEnd)
        #             index = newEnd + 1
                
        # root = TrieNode()
        # if not data:
        #     return root
        # start = 0
        # end = len(data) - 1
        # helper(root, data, start, end)
        # return root
        
        root = TrieNode()
        queue = []
        current = root
        for s in data:
            if s == '<':
                queue.append(current)
            elif s == '>':
                queue.pop()
            else:
                current = TrieNode()
                queue[-1].children[s] = current
        return root
                
