class Solution {
public:
    /**
     * @param nums: A list of integers.
     * @return: An integer denotes the middle number of the array.
     */
    int median(vector<int> &nums) {
        // write your code here
        auto target = nums.begin() + (nums.size() - 1) / 2;
        nth_element(nums.begin(), target, nums.end());
        return *target;
    }
};
