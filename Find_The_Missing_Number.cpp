class Solution {
public:
    /**    
     * @param nums: a vector of integers
     * @return: an integer
     */
    int findMissing(vector<int> &nums) {
        // write your code here
        int result = 0;
        for(auto& num : nums){
            result ^= num;
        }
        for(int i = 0; i < nums.size() + 1; ++i){
            result ^= i;
        }
        return result;
    }
};
