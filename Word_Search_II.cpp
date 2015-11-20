class Solution {
private:
    struct TrieNode
    {
        bool isString = false;
        unordered_map<char, TrieNode *> leaves;
        
        bool insert(const string &s)
        {
            auto* p = this;
            for (const auto &c : s)
            {
                if (p->leaves.find(c) == p->leaves.cend())
                {
                    p->leaves[c] = new TrieNode;
                }
                p = p->leaves[c];
            }
            
            if (p->isString)
            {
                return false;//show already exists.
            }
            else
            {
                p->isString = true;
                return true;
            }
        }
        
        ~TrieNode()
        {
            for (auto &kv : leaves)
            {
                if(kv.second)
                {
                    kv.second->~TrieNode();
                }
            }
        }
    };
    
public:
    /**
     * @param board: A list of lists of character
     * @param words: A list of string
     * @return: A list of string
     */
    vector<string> wordSearchII(vector<vector<char> > &board, vector<string> &words) {
        // write your code here
        unordered_set<string> ret;
        TrieNode trie;
        for (const auto &w : words)
        {
            trie.insert(w);
        }
        string curr;
        vector<vector<bool>> visited(board.size(), vector<bool>(board[0].size(), false));
        for (int row = 0; row < board.size(); ++row)
        {
            for (int col = 0; col < board[0].size(); ++col)
            {
                doSearchDFS(row, col, curr, visited, &trie, board, ret);    
            }
        }
        
        return vector<string>(ret.begin(), ret.end());
    }
    
    //you dont know if a reference is invalid
    void doSearchDFS(int row, int col, string &curr, vector<vector<bool>> &visited, TrieNode *trie, const vector<vector<char>> &board, unordered_set<string> &ret)
    {
        if (!trie || row < 0 || row >= board.size() || col < 0 || col >= board[0].size())
        {
            return;
        }
        
        if(!trie->leaves[board[row][col]] || visited[row][col])
        {
            return;
        }
        
        TrieNode *next = trie->leaves[board[row][col]];
        curr.push_back(board[row][col]);
        if (next->isString)
        {
            ret.insert(curr);
        }
        
        visited[row][col] = true;
        vector<pair<int, int>> dictions{{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        for (int i = 0; i < 4; ++i)
        {
            doSearchDFS(row + dictions[i].first, col + dictions[i].second, curr, visited, next, board, ret);
        }
        visited[row][col] = false;
        curr.pop_back();
    }
};
