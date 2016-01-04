class Solution {
public:
    /**
     * @param nums: a vector of integers
     * @return: the maximum difference
     */
    struct Bucket {
        long long min = static_cast<long long>(INT_MAX) + 1;
        long long max = static_cast<long long>(INT_MIN) - 1;
    };
    int maximumGap(vector<int> nums) {
        // write your code here
        if (nums.empty() || nums.size() == 1)
        {
            return 0;
        }
        int nums_min = *min_element(nums.cbegin(), nums.cend());
        int nums_max = *max_element(nums.cbegin(), nums.cend());
        int gap = max(1, (nums_max - nums_min) / (static_cast<int>(nums.size()) - 1));
        vector<Bucket> buckets((nums_max - nums_min) / gap + 1);
        for (const auto &n : nums)
        {
            int index = (n - nums_min) / gap;
            buckets[index].min = min(buckets[index].min, static_cast<long long>(n));
            buckets[index].max = max(buckets[index].max, static_cast<long long>(n));
        }
        int max_gap = 0, pre_max = nums_min;
        for (const auto &b : buckets)
        {
            if (b.min != static_cast<long long>(INT_MAX) + 1)
            {
                max_gap = max(max_gap, static_cast<int>(b.min) - pre_max);
                pre_max = b.max;
            }
        }
        return max_gap;
        
    }
};