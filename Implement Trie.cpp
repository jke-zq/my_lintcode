/**
 * Your Trie object will be instantiated and called as such:
 * Trie trie;
 * trie.insert("lintcode");
 * trie.search("lint"); will return false
 * trie.startsWith("lint"); will return true
 */
class TrieNode {
public:
    // Initialize your data structure here.
    TrieNode():isStr(false) {
        
    }
    bool isStr;
    unordered_map<char, TrieNode *> leaves;
};

class Trie {
public:
    Trie() {
        root = new TrieNode();
    }

    // Inserts a word into the trie.
    void insert(string word) {
        auto *p = root;
        for (const char &c : word)
        {
            if (p->leaves.find(c) == p->leaves.end())
            {
                p->leaves[c] = new TrieNode();
            }
            p = p->leaves[c];
        }
        p->isStr = true;
    }

    // Returns if the word is in the trie.
    bool search(string word) {
        TrieNode *node = find(word, root);
        if (node)
        {
            return node->isStr;
        }
        else
        {
            return false;
        }
    }

    // Returns if there is any word in the trie
    // that starts with the given prefix.
    bool startsWith(string prefix) {
        return find(prefix, root) != nullptr;
    }
    TrieNode *find(string word, TrieNode *node)
    {
        auto *p = root;
        for (const auto & c : word)
        {
            if (p->leaves.find(c) != p->leaves.end())
            {
                p = p->leaves[c];
            }
            else
            {
                return nullptr;
            }
        }
        return p;
    }
private:
    TrieNode* root;
};