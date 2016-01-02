class Solution {
public:
    /**
     * @param board: A list of lists of character
     * @param word: A string
     * @return: A boolean
     */
    bool exist(vector<vector<char> > &board, string word) {
        // write your code here
        
        if (board.empty())
        {
            return false;
        }
        vector<vector<bool>> visited(board.size(), vector<bool>(board[0].size(), false));
        for (int i = 0; i < board.size(); ++i)
        {
            for (int j = 0; j < board[0].size(); ++j)
            {
                if (search(i, j, 0, visited, word, board))
                {
                    return true;
                }
            }
        }
        return false;
    }
    bool search(int row, int col, int start, vector<vector<bool>> &visited, const string &word, const vector<vector<char>> &board)
    {
        if (start == word.length())
        {
            return true;
        }
        if (row < 0 || row >= board.size() || col < 0 || col >= board[0].size() || visited[row][col])
        {
            return false;
        }
        
        if (word[start] != board[row][col])
        {
            return false;
        }
        
        visited[row][col] = true;
        vector<pair<int, int>> dicts{{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        for (const auto &p : dicts)
        {
            if (search(row + p.first, col + p.second, start + 1, visited, word, board))
            {
                return true;
            }
        }
        visited[row][col] = false;
        return false;
        
        
        
    }
};