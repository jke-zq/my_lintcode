class Solution {
public:    
    /**
     * @param numbers: Give an array numbers of n integer
     * @param target: An integer
     * @return: return the sum of the three integers, the sum closest target.
     */
    int threeSumClosest(vector<int> nums, int target) {
        // write your code here
        sort(nums.begin(), nums.end());
        int length = nums.size();
        int left = 0;
        int ret = INT_MIN;
        int start = 0, end = 0;
        for (int i = 0; i < length - 2; ++i){
            left = target - nums[i];
            start = i + 1;
            end = length - 1;
            while (start < end){
                if (nums[start] + nums[end] == left) return target;
                ret = abs(target -ret) > abs(left - nums[start] - nums[end]) ? nums[i] + nums[start] + nums[end] : ret;
                if (nums[start] + nums[end] > left) --end;
                if (nums[start] + nums[end] < left) ++start;
            }
        }
        return ret;
    }
};

