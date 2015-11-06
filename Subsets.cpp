class Solution {
public:
    /**
     * @param S: A set of numbers.
     * @return: A list of lists. All valid subsets.
     */
    vector<vector<int> > subsets(vector<int> &nums) {
    	// write your code here
    	vector<vector<int>> ret;
    	vector<int> solution;
    	sort(nums.begin(), nums.end());
    	helper(0, solution, nums, ret);
    	return ret;
    }
private:
    void helper(int start, vector<int> &solution, const vector<int> &nums, vector<vector<int>> &ret)
    {
        ret.emplace_back(solution);
        for (int i = start; i < nums.size(); ++i)
        {
            solution.emplace_back(nums[i]);
            helper(i + 1, solution, nums, ret);
            solution.pop_back();
        }
    }
};
