class Solution {
public:
    /**
     * @param nums: A list of integers
     * @return an integer
     */
    int longestConsecutive(vector<int> &num) {
        // write you code here
        unordered_set<int> entries;
        for (const auto &n : num)
        {
            entries.insert(n);
        }
        int result = 0;
        while (!entries.empty())
        {
            auto n = *entries.begin();
            entries.erase(n);
            int lower = n - 1;
            while (entries.count(lower))
            {
                entries.erase(lower);
                --lower;
            }
            int upper = n + 1;
            while (entries.count(upper))
            {
                entries.erase(upper);
                ++upper;
            }
            result = max(result, upper - lower - 1);
        }
        return result;
    }
};
