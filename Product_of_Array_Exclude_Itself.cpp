class Solution {
public:
    /**
     * @param A: Given an integers array A
     * @return: A long long array B and B[i]= A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1]
     */
    vector<long long> productExcludeItself(vector<int> &nums) {
        // write your code here
        if (nums.size() < 2) return vector<long long>(1, 1);
        
        vector<long long> leftProduct(nums.size());
        vector<long long> rightProduct(nums.size());
        
        leftProduct[0] = 1;
        for (int i = 1; i < nums.size(); ++i){
            leftProduct[i] = leftProduct[i - 1] * nums[i - 1];
        }
        
        rightProduct[nums.size() - 1] = 1;
        for (int i = nums.size() - 2; i >= 0; --i){
            rightProduct[i] = rightProduct[i + 1] * nums[i + 1];
        }
        
        vector<long long> ret(nums.size());
        for (int i = 0; i < nums.size(); ++i){
            ret[i] = leftProduct[i] * rightProduct[i];
        }
        return ret;
    }
};
