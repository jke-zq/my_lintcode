class Solution {
public:    
    /**
     * @param S, T: Two string.
     * @return: Count the number of distinct subsequences
     */
    int numDistinct(string &S, string &T) {
        // write your code here
        const int s_len = S.length();
        const int t_len = T.length();
        // vector<vector<int>> table(2, vector<int>(s_len + 1, 0));
        // table[0][0] = 1;
        // for (int i = 1; i < t_len + 1; ++i){
        //     table[i % 2][0] = 0;
        //     for (int j = 1; j < s_len + 1; ++j){
        //         table[i % 2][j] = table[i % 2][j - 1];
        //         if (T[i - 1] == S[j - 1]){
        //             table[i % 2][j] += table[(i - 1)% 2][j - 1] == 0 && i == 1 ? 1 : table[(i - 1)% 2][j - 1];
        //         }

        //     }
        // }
        // return table[t_len % 2][s_len];
        //other solution, the other way
        vector<vector<int>> table(2, vector<int>(t_len + 1, 0));
        table[0][0] = 1;
        for (int i = 1; i < s_len + 1; ++i){
            table[i % 2][0] = 1;// table[i % 2][0] = table[(i - 1) % 2][0];
            for (int j = 1; j < t_len + 1; ++j){
                // table[i % 2][j] += table[(i - 1)][j];
                table[i %2][j] = S[i - 1] == T[j - 1] ? table[(i - 1) % 2][j] + table[(i - 1) % 2][j - 1] : table[(i - 1) % 2][j];
            }
        }
        return table[s_len % 2][t_len];
    }
};

