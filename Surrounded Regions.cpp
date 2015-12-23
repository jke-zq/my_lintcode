class Solution {
public:
    /**
     * @param board a 2D board containing 'X' and 'O'
     * @return void
     */
    void surroundedRegions(vector<vector<char>>& board) {
        // Write your code here
        //iterator
        if (board.empty())
        {
            return;
        }
        int rows = board.size();
        int cols = board[0].size();
        queue<pair<int, int>> q;
        for (int r = 0; r < rows; ++r)
        {
            q.emplace(make_pair(r, 0));
            q.emplace(make_pair(r, cols - 1));
        }
        for (int c = 0; c < cols; ++c)
        {
            q.emplace(make_pair(0, c));
            q.emplace(make_pair(rows - 1, c));
        }
        
        while (!q.empty())
        {
            int r, c;
            tie(r, c) = q.front();
            q.pop();
            if (board[r][c] == 'O')
            {
                board[r][c] = 'a';
                const vector<pair<int, int>> dicts{{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
                for (const auto& d : dicts)
                {
                    const int n_r = r + d.first, n_c = c + d.second;
                    if (n_r >= 0 && n_r < rows && n_c >= 0 && n_c < cols && board[n_r][n_c] == 'O')
                    {
                        q.emplace(make_pair(n_r, n_c));
                    }
                }
            }
        }
        
        //why wrong answer? If u know, plz tell me.
        // int rows = board.size();
        // int cols = board[0].size();
        // for (int r = 0; r < rows; ++r)
        // {
        //     dfs_c_a(r, 0, rows, cols, board);
        //     dfs_c_a(r, cols - 1, rows, cols, board);
        // }
        // for (int c = 0; c < cols; ++c)
        // {
        //     dfs_c_a(0, c, rows, cols, board);
        //     dfs_c_a(rows - 1, c, rows, cols, board);
        // }
        for (int r = 0; r < rows; ++r)
        {
            for (int c = 0; c < cols; ++c)
            {
                if (board[r][c] == 'O')
                {
                    board[r][c] = 'X';
                }
                else if (board[r][c] == 'a')
                {
                    board[r][c] = 'O';
                }
            }
        }
    }
    void dfs_c_a(int r, int c, int rows, int cols, vector<vector<char>> &board)
    {
        if (r < 0 || r >= rows || c < 0 || c >= cols || board[r][c] != 'O')
        {
            return;
        }
        board[r][c] == 'a';
        vector<pair<int, int>> pairs{{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
        for (auto &p : pairs)
        {
            dfs_c_a(r + p.first, c + p.second, rows, cols, board);
        }
        // dfs_c_a(r + 1, c, rows, cols, board);
        // dfs_c_a(r - 1, c, rows, cols, board);
        // dfs_c_a(r, c + 1, rows, cols, board);
        // dfs_c_a(r, c - 1, rows, cols, board);
    }
};