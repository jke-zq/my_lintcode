class Solution {
public:
    /**
     * @param m: An integer m denotes the size of a backpack
     * @param A: Given n items with size A[i]
     * @return: The maximum size
     */
    int backPack(int m, vector<int> A) {
        // write your code here
        //TLE: 8/9 case
        if (m > 20000){
            int sum_of_elements = 0;
            for_each(A.begin(), A.end(), [&](int n){ sum_of_elements += n;});
            if (sum_of_elements <= m) return sum_of_elements;
        }
        // table[i][j] denote the first i elements can fill the backpack j or not
        vector<vector<bool>> table(2, vector<bool>(m + 1, false));
        int maxsize = 0;
        table[0][0] = true;
        for (int i = 1; i < A.size() + 1; ++i){
            table[i % 2][0] = true;
            for (int j = 1; j < m + 1; ++j){
                table[i % 2][j] = table[(i - 1) % 2][j];
                if (j >= A[i - 1]){
                    table[i % 2][j] = table[i % 2][j] || table[(i - 1) % 2][j - A[i - 1]];
                }
                if (table[i % 2][j]) maxsize = max(maxsize, j);
            }
        }
        return maxsize;
       
    }
};
