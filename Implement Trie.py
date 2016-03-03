"""
Your Trie object will be instantiated and called as such:
trie = Trie()
trie.insert("lintcode")
trie.search("lint") will return false
trie.startsWith("lint") will return true
"""
class TrieNode:
  def __init__(self):
    # Initialize your data structure here.
    self.isStr = False
    self.chars = {}

class Trie:
  def __init__(self):
    self.root = TrieNode()

  # @param {string} word
  # @return {void}
  # Inserts a word into the trie.
  def insert(self, word):
      
      
      p = self.root
      for w in word:
          if w not in p.chars:
              p.chars[w] = TrieNode()
          p = p.chars[w]
      p.isStr = True
    
           
              
  # @param {string} word
  # @return {boolean}
  # Returns if the word is in the trie.
  def search(self, word):
      node = self.findNode(word)
      return bool(node and node.isStr)

  # @param {string} prefix
  # @return {boolean}
  # Returns if there is any word in the trie
  # that starts with the given prefix.
  def startsWith(self, prefix):
      return self.findNode(prefix) != None
      
  def findNode(self, word):
      p = self.root
      for w in word:
          if w in p.chars:
              p = p.chars[w]
          else:
              return None
      return p