class Solution {
public:
    /**
     * @param A an integer array
     * @return  A list of integers includes the index of 
     *          the first number and the index of the last number
     */
    vector<int> continuousSubarraySumII(vector<int>& A) {
        // Write your code here
        vector<int> nocircle(2);
        vector<int> circle(2);
        if (findnocircle(A, nocircle) > findcircle(A, circle))
        {
            return nocircle;
        }
        else
        {
            return circle;
        }
    }
    
    int findnocircle(vector<int> &A, vector<int> &nocircle)
    {
        int left = 0, right = 0;
        int pre_left = 0;
        int sum = 0;
        int max_size = INT_MIN;
        for (int i = 0; i < A.size(); ++i)
        {
            sum += A[i];
            if (max_size < sum)
            {
                max_size = sum;
                right = i;
                left = pre_left;
            }
            if (sum < 0)
            {
                sum = 0;
                pre_left = i + 1;
            }
        }
        nocircle[0] = left;
        nocircle[1] = right;
        return max_size;
    }
    
    int findcircle(vector<int> &A, vector<int> &circle)
    {
        int size = A.size();
        vector<int> max_to_left(size);
        vector<int> max_left_index(size);
        int sum = 0;
        for (int i = 0; i < A.size(); ++i)
        {
            sum += A[i];
            if (i == 0 || sum > max_to_left[i - 1])
            {
                max_to_left[i] = sum;
                max_left_index[i] = i;
            }
            else
            {
                max_to_left[i] = max_to_left[i - 1];
                max_left_index[i] = max_left_index[i - 1];
            }
        }
        vector<int> max_to_right(size);
        vector<int> max_right_index(size);
        sum = 0;
        for (int i = size - 1; i >= 0; --i)
        {
            sum += A[i];
            if (i == size - 1 || sum > max_to_right[i + 1])
            {
                max_to_right[i] = sum;
                max_right_index[i] = i;
            }
            else
            {
                max_to_right[i] = max_to_right[i + 1];
                max_right_index[i] = max_right_index[i + 1];
            }
        }
        int max_size = INT_MIN;
        for (int i = 0; i < size - 1; ++i)
        {
            if (max_to_left[i] + max_to_right[i + 1] > max_size)
            {
                max_size = max_to_left[i] + max_to_right[i + 1];
                circle[1] = max_left_index[i];
                circle[0] = max_right_index[i + 1];
            }
        }
        return max_size;
        
    }
};