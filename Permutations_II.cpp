class Solution {
public:
    /**
     * @param nums: A list of integers.
     * @return: A list of unique permutations.
     */
    vector<vector<int> > permuteUnique(vector<int> &nums) {
        // write your code here
        vector<vector<int>> ret;
        int len = nums.size();
        if (len == 0)
        {
            return ret;
        }
        sort(nums.begin(), nums.end());
        vector<bool> used(len, false);
        vector<int> tmp;
        doHelper(0, len, tmp, used, nums, ret);
        return ret;
    }
private:
    void doHelper(int has, int len, vector<int> &tmp, vector<bool> &used, const vector<int> &nums, vector<vector<int>> &ret)
    {
        if (has == len)
        {
            ret.emplace_back(tmp);
        }
        for (int i = 0; i < len; ++i)
        {
            if (used[i] || (i > 0 && nums[i] == nums[i - 1] && used[i - 1]))
            {
                continue;
            }
            used[i] = true;
            tmp.emplace_back(nums[i]);
            doHelper(has + 1, len, tmp, used, nums, ret);
            used[i] = false;
            tmp.pop_back();
        }
        
    }
};
