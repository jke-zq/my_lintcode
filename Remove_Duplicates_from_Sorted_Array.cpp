class Solution {
public:
    /**
     * @param A: a list of integers
     * @return : return an integer
     */
    int removeDuplicates(vector<int> &nums) {
        // write your code here
        // if (nums.size() == 0) return 0;
        // int front = 1;
        // int back = 0;
        // while (front < nums.size()){
        //     if (nums[back] != nums[front]){
        //         back++;
        //         int tmp = nums[back];
        //         nums[back] = nums[front];
        //         nums[front] = tmp;
        //     }
        //     front++;
        // }
        // return back + 1;
        // look this
        if (nums.empty()) return 0;
        int right = 1;
        int left = 0;
        while (right < nums.size()){
            if (nums[left] != nums[right]){
                left++;
                nums[left] = nums[right];
            }
            right++;
        }
        return left + 1;
    }
};
