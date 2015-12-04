class Solution {
public:
    /**
     * @param nums: A list of integers.
     * @return: The median of the element inside the window at each moving
     */
    vector<int> medianSlidingWindow(vector<int> &nums, int k) {
        // write your code here
        vector<int> ret;
        multiset<int, less<int>> min_set;
        multiset<int, greater<int>> max_set;
        for (int i = 0; i < nums.size(); ++i)
        {
            if (i >= k)
            {
                //duplicates
                // min_set.erase(nums[i - k]);
                // max_set.erase(nums[i - k]);
                // Remove the element outside the window.
                //first find from max_set to ensure min_set has the max numbers
                if (max_set.find(nums[i - k]) != max_set.cend()) {
                    max_set.erase(max_set.find(nums[i - k]));
                } else {
                    min_set.erase(min_set.find(nums[i - k]));
                }
            }
            if (max_set.empty() || *max_set.cbegin() < nums[i])
            {
                min_set.emplace(nums[i]);
                if (min_set.size() > max_set.size() + 1)
                {
                    max_set.emplace(*min_set.cbegin());
                    min_set.erase(min_set.begin());
                }
            }
            else
            {
                max_set.emplace(nums[i]);
                if (max_set.size() > min_set.size())
                {
                    min_set.emplace(*max_set.cbegin());
                    max_set.erase(max_set.begin());
                }
            }
            
            if (i >= k - 1)
            {
                ret.emplace_back(min_set.size() > max_set.size() ? *min_set.cbegin() : *max_set.cbegin());
            }
        }
        return ret;
    }
};

