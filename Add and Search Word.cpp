class WordDictionary {
 
public:
    struct TrieNode {
        bool isStr = false;
        unordered_map<char, TrieNode *> leaves;
    };
    WordDictionary()
    {
        _root = new TrieNode();
        // _root->isStr = true;
    }

    // Adds a word into the data structure.
    void addWord(string word) {
        // Write your code here
        auto *p = _root;
        for (const auto &c : word)
        {
            if (p->leaves.find(c) == p->leaves.end())
            {
                p->leaves[c] = new TrieNode();
            }
            p = p->leaves[c];
        }
        p->isStr = true;
    }

    // Returns if the word is in the data structure. A word could
    // contain the dot character '.' to represent any one letter.
    bool search(string word) {
        // Write your code here
        return search(word, _root, 0);
    }
    bool search(string word, TrieNode *node, int length)
    {
        if (length == word.length())
        {
            return node->isStr;
        }
        else
        {
            if (node->leaves.find(word[length]) != node->leaves.end())
            {
                return search(word, node->leaves[word[length]], length + 1);
            }
            else if (word[length] == '.')
            {
                for (const auto &k : node->leaves)
                {
                    if (search(word, k.second, length + 1))
                    {
                        return true;
                    }
                }
                return false;
            }
            else
            {
                return false;
            }
        }
    }
    
private:
    TrieNode *_root;
   
};

// Your WordDictionary object will be instantiated and called as such:
// WordDictionary wordDictionary;
// wordDictionary.addWord("word");
// wordDictionary.search("pattern");