class Solution {
public:
    /**
     * @param nums: A list of integers.
     * @return: A list of permutations.
     */
    vector<vector<int> > permute(vector<int> nums) {
        // write your code here
        vector<vector<int>> ret;
        if (nums.empty())
        {
            return ret;
        }
        sort(nums.begin(), nums.end());
        do
        {
            ret.emplace_back(nums);
        } while (nextPermutation(nums));
        return ret;
    }
    bool nextPermutation(vector<int> &nums)
    {
        int len = nums.size();
        int i = len - 1;
        while (i > 0 && nums[i] < nums[i - 1])
        {
            --i;
        }
        
        if (i > 0)
        {
            int j = len - 1;
            while (nums[j] < nums[i - 1])
            {
                --j;
            }
            swap(nums[i - 1], nums[j]);
            reverse(nums.begin() + i, nums.end());
            return true;
        }
        else
        {
            return false;
        }
        
    }
};

