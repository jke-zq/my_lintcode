class Solution {
public:    
    /**
     * @param word1 & word2: Two string.
     * @return: The minimum number of steps.
     */
    int minDistance(string word1, string word2) {
        // write your code here
        const size_t m = word1.size();
        const size_t n = word2.size();
        if (m < n) return minDistance(word2, word1);
        vector<vector<int>> table(2, vector<int>(n + 1, 0));
        for (int i = 0; i < n + 1; ++i) table[0][i] = i;
        
        for (int i = 1; i < m + 1; ++i){
            table[i % 2][0] = i;
            for (int j = 1; j < n + 1; ++j){
                table[i % 2][j] = word1[i - 1] == word2[j - 1] ? table[(i - 1) % 2][j - 1] :
                 1 + min(table[(i - 1) % 2][j - 1], min(table[(i - 1) % 2][j], table[i % 2][j - 1]));
            }
        }
        return table[m % 2][n];
    }
};

