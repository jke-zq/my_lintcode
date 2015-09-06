class Solution {
public:
    /**
     * @param A: An integer array.
     * @param target: An integer.
     */
    int MinAdjustmentCost(vector<int> A, int target) {
        // write your code here
        int nums_len = A.size();
        int MAX_NUM = 100;
        vector<vector<int>> table(2, vector<int>(MAX_NUM + 1));
        for (int i = 1; i < nums_len + 1; ++i){
            for ( int j = 1; j < MAX_NUM + 1; ++j){
                // the i - 1 element can change to [down, up].
                int up = min(MAX_NUM, j + target);
                int down = max(1, j - target);
                table[i % 2][j] = INT_MAX;
                // for (int k = down; k <= up; ++k){
                table[i % 2][j] = *min_element(next(table[(i - 1) % 2].cbegin(), down), next(table[(i - 1) % 2].cbegin(), up + 1)) + abs(A[i - 1] - j);
                    // table[i % 2][j] = min(table[i % 2][j], table[(i - 1) % 2][k]);
                // }
                // table[i % 2][j] += abs(A[i - 1] - j);
            }
        }
        // not table[n][0], j from 1 to 100
        return *min_element(next(table[nums_len % 2].cbegin()), table[nums_len % 2].cend());
        
    }
};
