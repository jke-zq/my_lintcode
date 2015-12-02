class Solution {
public:
    /**
     * @param A an integer array
     * @return  A list of integers includes the index of 
     *          the first number and the index of the last number
     */
    vector<int> continuousSubarraySum(vector<int>& A) {
        // Write your code here
        int sum = 0;
        int left = 0, right = 0, pre_left = 0;
        int max = INT_MIN;
        for (int i = 0; i < A.size(); ++i)
        {
            sum += A[i];
            if (max < sum)
            {
                max = sum;
                right = i;
                left = pre_left;
            }
            if (sum < 0)
            {
                sum = 0;
                pre_left = i + 1;
            }
        }
        return {left, right};
    }
};
