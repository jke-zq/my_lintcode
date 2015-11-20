class Solution {
public:
    /**
     * @param height: A list of integer
     * @return: The area of largest rectangle in the histogram
     */
    int largestRectangleArea(vector<int> &height) {
        // write your code here
        //soooo ugly
        // int ret = 0;
        // stack<int> indexs;
        // height.emplace_back(0);
        // for (int i = 0; i < height.size(); ++i)
        // {
        //     if (indexs.empty())
        //     {
        //         indexs.emplace(i);
        //         continue;
        //     }
        //     if (height[indexs.top()] > height[i])
        //     {
        //         while (!indexs.empty() && height[indexs.top()] > height[i])
        //         {
        //             int last = indexs.top();
        //             indexs.pop();
        //             int top = -1;
        //             if (!indexs.empty())
        //             {
        //                 top = indexs.top();
        //             }
        //             ret = max(ret, (i - 1 - top) * height[last]);
                    
        //         }
        //     }

        //     indexs.emplace(i);
        // }
        // return ret;
        int max_area = 0;
        stack<int> increasing_height;
        int i = 0;
        while (i <= height.size())//equaling does matters
        {
            if (increasing_height.empty() || (i < height.size() && height[i] >= height[increasing_height.top()]))
            {
                increasing_height.emplace(i);
                ++i;
            }
            else
            {
                int last = increasing_height.top();
                increasing_height.pop();
                if (increasing_height.empty())
                {
                    max_area = max(max_area, (i - 1 - (-1)) * height[last]);
                }
                else
                {
                    max_area = max(max_area, (i - 1 - increasing_height.top()) * height[last]);
                }
            }
        }
        return max_area;
    }
};
