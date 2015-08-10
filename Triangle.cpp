class Solution {
public:
    /**
     * @param triangle: a list of lists of integers.
     * @return: An integer, minimum path sum.
     */
    int minimumTotal(vector<vector<int> > &triangle) {
        // write your code here
        int rows = triangle.size();
        vector<vector<int>> table(2);
        table[0].emplace_back(triangle[0][0]);
        for(int i = 1; i < rows; ++i){
            table[i%2].emplace_back(table[(i-1)%2][0] + triangle[i][0]);
            int j = 1;
            for(; j < triangle[i].size()-1; ++j){
                table[i%2].emplace_back(min(table[(i-1)%2][j-1], table[(i-1)%2][j]) + triangle[i][j]);
            }
            table[i%2].emplace_back(table[(i-1)%2][j-1] + triangle[i][j]);
            table[(i-1)%2].clear();
        }
        int ret = INT_MAX;
        for(auto& r : table[(rows-1)%2]){
            ret = min(ret, r);
        }
        return ret;
    }
};
