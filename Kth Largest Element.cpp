class Solution {
public:
    /*
     * param k : description of k
     * param nums : description of array and index 0 ~ n-1
     * return: description of return
     */
    int kthLargestElement(int k, vector<int> nums) {
        // write your code here
        ////////////////Time Limit Exceeded, without random////////////////
        // return quickSelect(nums.size() - k + 1, 0, nums.size() - 1, nums);
        ////////////copy the answer///////////////
        ///short one
        // nth_element(nums.begin(), nums.begin() + k - 1, nums.end(), greater<int>());
        // return nums[k - 1];
        ///quickselect with random
        int left = 0, right = nums.size() - 1;
        default_random_engine gen((random_device())());
        while (left <= right)
        {
            uniform_int_distribution<int> dis(left, right);
            int pivot = dis(gen);
            int new_pivot = partitionAroundPivot(left, right, pivot, nums);
            if (new_pivot > k - 1)
            {
                right = new_pivot - 1;
            }
            else if (new_pivot < k - 1)
            {
                left = new_pivot + 1;
            }
            else
            {
                return nums[new_pivot];
            }
            
        }
    }
    
    int partitionAroundPivot(int start, int end, int pivot, vector<int> &nums)
    {
        int pivot_val = nums[pivot];
        swap(nums[end], nums[pivot]);
        int new_pivot = start;
        for (int i = start; i < end; ++i)
        {
            if (nums[i] > pivot_val)
            {
                swap(nums[i], nums[new_pivot]);
                ++new_pivot;
            }
        }
        swap(nums[end], nums[new_pivot]);
        return new_pivot;
    }
    
    int quickSelect(int k, int start, int end, vector<int> &nums)
    {
        //quick sort
        int part = position(start, end, nums);
        if (part > k - 1)
        {
            return quickSelect(k, start, part - 1, nums);
        }
        else if (part < k - 1)
        {
            return quickSelect(k, part + 1, end, nums);
        }
        else
        {
            return nums[part];
        }
        
    }
    int position(int start, int end, vector<int> &nums)
    {

        int left = start;
        int right = end;
        int target = nums[left];
        while (left < right)
        {
            while (nums[right] > target && right > left)
            {
                --right;
            }
            if (right > left)
            {
                nums[left] = nums[right];   
            }
            while (nums[left] < target && right > left)
            {
                ++left;
            }
            if (right > left)
            {
                nums[right] = nums[left];
            }
        }
        nums[left] = target;
        return left;
    }
};
