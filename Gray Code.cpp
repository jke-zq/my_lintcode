class Solution {
public:
    /**
     * @param n a number
     * @return Gray code
     */
    vector<int> grayCode(int n) {
        // Write your code here
        vector<int> ret = {0};
        for (int i = 0; i < n; ++i)
        {
            for (int j = ret.size() - 1; j >= 0; --j)
            {
                ret.emplace_back((1 << i) + ret[j]);
            }
        }
        return ret;
    }
};