class Solution {
public:
    int partitionArray(vector<int> &nums, int k) {
        // write your code here
        
        int start = 0;
        int end = nums.size();
        while (start < end){
            while (start < end && nums[start] < k) ++start;
            while (start < end && nums[end - 1] >= k) --end;
            if (start < end){
                swap(nums[start], nums[end - 1]);
                ++start;
                --end;
            }
        }
        return start;
    }
};
