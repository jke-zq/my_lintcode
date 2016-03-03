class TrieNode:
    def __init__(self):
        self.isStr = False
        self.chars = {}

class WordDictionary:
    # initialize your data structure here.
    def __init__(self):
        # Write your code here
       self.root = TrieNode() 

    # @param {string} word
    # @return {void}
    # Adds a word into the data structure.
    def addWord(self, word):
        # Write your code here
        p = self.root
        for w in word:
            if w not in p.chars:
                p.chars[w] = TrieNode()
            p = p.chars[w]
        p.isStr = True


    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the data structure. A word could
    # contain the dot character '.' to represent any one letter.
    def search(self, word):
        # Write your code here
        def helper(start, length, word, trieNode):
            # if start == length or not trieNode:
            #     return bool(trieNode and trieNode.isStr)
            if start == length:
                return bool(trieNode and trieNode.isStr)
            else:
                if word[start] in trieNode.chars:
                    return helper(start + 1, length, word, trieNode.chars[word[start]])
                elif word[start] == '.':
                    for node in trieNode.chars.values():
                        if helper(start + 1, length, word, node):
                            return True
                    return False
                else:
                    return False
        if not word:
            return True
        length = len(word)
        return helper(0, length, word, self.root)

# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")