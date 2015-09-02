class Solution {
public:
    /**
     * @param m: An integer m denotes the size of a backpack
     * @param A & V: Given n items with size A[i] and value V[i]
     * @return: The maximum value
     */
    int backPackII(int m, vector<int> A, vector<int> V) {
        // write your code here
        //table[i][j] denotes the maxVal the backpack can get from the first i elements
        vector<vector<int>> table(2, vector<int>(m + 1, 0));
        for (int i = 1; i < A.size() + 1; ++i){
            for (int j = 1; j < m + 1; ++j){
                table[i % 2][j] = table[(i - 1) % 2][j];
                if (j >= A[i - 1]) table[i % 2][j] = max(table[(i - 1) % 2][j - A[i - 1]] + V[i - 1], table[i % 2][j]);
            }
        }
        return table[A.size() % 2][m];
    }
};
