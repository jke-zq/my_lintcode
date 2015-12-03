class Solution {
public:
    /**
     * @param nums: A list of integers.
     * @return: The maximum number inside the window at each moving.
     */
    vector<int> maxSlidingWindow(vector<int> &nums, int k) {
        // write your code here
        vector<int> ret;
        deque<int> que;
        if (!nums.size())
        {
            return ret;
        }
        for (int i = 0; i < k; ++i)
        {
            while (!que.empty() && nums[que.back()] < nums[i])
            {
                que.pop_back();
            }
            que.push_back(i);
        }
        
        for (int i = k; i < nums.size(); ++i)
        {
            ret.emplace_back(nums[que.front()]);
            while (!que.empty() && que.front() <= i - k)
            {
                que.pop_front();
            }
            while (!que.empty() && nums[que.back()] < nums[i])
            {
                que.pop_back();
            }
            que.push_back(i);
        }
        ret.emplace_back(nums[que.front()]);
        return ret;
        
    }
};

