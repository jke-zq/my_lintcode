class Solution {
public:
    /**
     * @param nums: A list of integers
     * @return: A list of integers includes the index of the first number 
     *          and the index of the last number
     */
    vector<int> subarraySumClosest(vector<int> nums){
        // write your code here
        int length = nums.size();
        vector<pair<int, int>> acc(length + 1, pair<int, int>(0, 0));
        acc[0].second = -1;//acc value, index
        for (int i = 1; i < length + 1; ++i){
            acc[i].first = acc[i - 1].first + nums[i - 1];
            acc[i].second = i - 1;
        }
        
        sort(acc.begin(), acc.end());
        
        int min_diff = INT_MAX;
        int min_index = 0;
        int max_index = 0;
        for (int i = 1; i < length + 1; ++i){
            int diff = abs(acc[i].first - acc[i - 1].first);
            if (min_diff > diff){
                min_diff = diff;
                min_index = min(acc[i].second, acc[i - 1].second) + 1;
                max_index = max(acc[i].second, acc[i - 1].second);
            }
        }
        return {min_index, max_index};
    }
};

