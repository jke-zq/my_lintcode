class Solution {
public:
    /**
     * @param heights: a vector of integers
     * @return: a integer
     */
    int trapRainWater(vector<int> &heights) {
        // write your code here
        //I cant sovle this problem. I think if you can find compare between the left and right heights(that the left and right are not close is not required), you can solve it.
        //solution one:
        //find the heightest one, as the right part from left, as the left part from right.
        // if (heights.empty())
        // {
        //     return 0;
        // }
        // int top_index = 0;
        // for (int i = 0; i < heights.size(); ++i)
        // {
        //     if (heights[top_index] < heights[i])
        //     {
        //         top_index = i;
        //     }
        // }
        // int ret = 0;
        // int left = 0;
        // int left_top = 0;
        // while (left < top_index)
        // {
        //     left_top = max(left_top, heights[left]);
        //     ret += left_top - heights[left];
        //     ++left;
        // }
        // int right = heights.size() - 1;
        // int right_top = 0;
        // while (right > top_index)
        // {
        //     right_top = max(right_top, heights[right]);
        //     ret += right_top - heights[right];
        //     --right;
        // }
        // return ret;
        //solution two:
        //the leftmost and the rightmost all can be the right or left part to each other.
        if (heights.empty())
        {
            return 0;
        }
        int left = 0;
        int right = heights.size() - 1;
        int left_top = heights[left], right_top = heights[right];
        int ret = 0;
        while (left < right)
        {
            if (heights[left] < heights[right])
            {
                ++left;
                left_top = max(left_top, heights[left]);
                ret += left_top - heights[left];
            }
            else
            {
                --right;
                right_top = max(right_top, heights[right]);
                ret += right_top - heights[right];
            }
        }
        return ret;
    }
};