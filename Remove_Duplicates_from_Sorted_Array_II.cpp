class Solution {
public:
    /**
     * @param A: a list of integers
     * @return : return an integer
     */
    int removeDuplicates(vector<int> &nums) {
        // write your code here
        int left = -1;
        int right = 0;
        int length = nums.size();
        while (right < length){
            if (left == -1 || nums[right] != nums[left]){
                nums[++left] = nums[right];
                ++right;
                if (right < length && nums[right] == nums[right - 1]){
                    nums[++left] = nums[right++];
                }
            }else{
                ++right;
            }
        }
        return left + 1;
    }
};
