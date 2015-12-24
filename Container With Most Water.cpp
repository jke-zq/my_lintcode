class Solution {
public:
    /**
     * @param heights: a vector of integers
     * @return: an integer
     */
    int maxArea(vector<int> &heights) {
        // write your code here
        if (heights.empty())
        {
            return 0;
        }
        int i = 0, j = heights.size() - 1;
        int max_area = INT_MIN;
        while (i < j)
        {
            max_area = max(max_area, min(heights[i], heights[j]) * (j - i));
            if (heights[i] > heights[j])
            {
                --j;
            }
            else
            {
                ++i;
            }
        }
        return max_area;
    }
};