class Solution {
public:
    /**
     * @param candidates: A list of integers
     * @param target:An integer
     * @return: A list of lists of integers
     */
    vector<vector<int> > combinationSum(vector<int> &candidates, int target) {
        // write your code here
        vector<vector<int>> ret;
        vector<int> solution;
        sort(candidates.begin(), candidates.end());
        helper(0, candidates, target, solution, ret);
        return ret;
    }
private:
    void helper(int start, vector<int> &candidates, int left, vector<int> &solution, vector<vector<int>> &ret)
    {
        if (left == 0){
            ret.emplace_back(solution);
            return;
        }
        else if (left < 0)
        {
            return;
        }
        for (int i = start; i < candidates.size(); ++i)
        {
            if (i > 0 && candidates[i] == candidates[i - 1])
            {
                continue;
            }
            solution.emplace_back(candidates[i]);
            helper(i, candidates, left - candidates[i], solution, ret);
            solution.pop_back();
        }
    }
};
