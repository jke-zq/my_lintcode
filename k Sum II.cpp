class Solution {
public:
    /**
     * @param A: an integer array.
     * @param k: a positive integer (k <= length(A))
     * @param target: a integer
     * @return a list of lists of integer 
     */
    vector<vector<int> > kSumII(vector<int> A, int k, int target) {
        // write your code here
        vector<vector<int>> ret;
        if (A.empty())
        {
            return ret;
        }
        sort(A.begin(), A.end());
        vector<int> tmp;
        dfs(0, tmp, k, target, A, ret);
        return ret;
    }
    void dfs(int start, vector<int> &tmp, int k, int target, vector<int> &A, vector<vector<int>> &ret)
    {
        if (k == 0)
        {
            if (target == 0)
            {
                ret.emplace_back(tmp);
            }
            return;
        }
        for (int i = start; i < A.size() - k + 1; ++i)
        {
            if (A[i] > target)
            {
                return;
            }
            tmp.emplace_back(A[i]);
            dfs(i + 1, tmp, k - 1, target - A[i], A, ret);
            tmp.pop_back();
        }
        
    }
};
