class Solution {
public:
    /**
     * @param nums: A list of integers
     * @return: The majority number
     */
    int majorityNumber(vector<int> nums) {
        // write your code here
        int ans = nums[0], cnt = 0;
        for (const auto& i : nums){
            if (ans == i){
                ++cnt;
            }else{
                --cnt;
                if (cnt == 0){
                    ans = i;
                    ++cnt;
                }
            }
        }
        return ans;
    }
};
