class Solution {
public:
    /**
     * @param S: A set of numbers.
     * @return: A list of lists. All valid subsets.
     */
    vector<vector<int> > subsetsWithDup(const vector<int> &S) {
        // write your code here
        vector<vector<int>> ret;
        vector<int> solution;
        vector<int> sorted_S(S);
        sort(sorted_S.begin(), sorted_S.end());
        helper(0, solution, sorted_S, ret);
        return ret;
    }
    
private:
    void helper(int start, vector<int> &solution, const vector<int> &S, vector<vector<int>> 
    &ret)
    {
        ret.emplace_back(solution);
        for (int i = start; i < S.size(); ++i)
        {
            if ( i > start && S[i - 1] == S[i])
            {
                continue;
            }
            solution.emplace_back(S[i]);
            helper(i + 1, solution, S, ret);
            solution.pop_back();
        }
    }
};

