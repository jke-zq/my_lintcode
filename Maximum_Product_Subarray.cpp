class Solution {
public:
    /**
     * @param nums: a vector of integers
     * @return: an integer
     */
    int maxProduct(vector<int>& nums) {
        // write your code here
        //Time Limit Exceeded
        // const int n = nums.size();
        // int ret = INT_MIN;
        // for (int i = 0; i < n; ++i){
        //     int s = 1;
        //     for ( int j = i; j < n; ++j){
        //         s *= nums[j];
        //         ret = max(s, ret);
        //     }
        // }
        // return ret;
        
        int ret = INT_MIN, local_max = 1, local_min = 1;
        for (auto& n : nums){
            int cur_max = local_max * n;
            int cur_min = local_min * n;
            local_max = max(n, max(cur_min, cur_max));
            local_min = min(n, min(cur_min, cur_max));
            ret = max(ret, local_max);
        }
        return ret;

    }
};
