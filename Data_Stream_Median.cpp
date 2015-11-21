class Solution {
public:
    /**
     * @param nums: A list of integers.
     * @return: The median of numbers
     */
    vector<int> medianII(vector<int> &nums) {
        // write your code here
        //copy completely
        //familiar with the data struct.
        //using multiset
        // multiset<int, less<int>> min_set;
        // multiset<int, greater<int>> max_set;
        // vector<int> ret;
        // for (auto &n : nums)
        // {
        //     if (max_set.empty() || n > *min_set.cbegin())
        //     {
        //         min_set.insert(n);
        //         if (min_set.size() > max_set.size() + 1)
        //         {
        //             max_set.insert(*min_set.cbegin());
        //             min_set.erase(min_set.cbegin());
        //         }
        //     }
        //     else
        //     {
        //         max_set.insert(n);
        //         if (max_set.size() > min_set.size())
        //         {
        //             min_set.insert(*max_set.cbegin());
        //             max_set.erase(max_set.cbegin());
        //         }
        //     }
        //     ret.emplace_back(max_set.size() == min_set.size() ? *max_set.cbegin() : *min_set.cbegin());
        // }
        // return ret;
        //using priority_queue
        priority_queue<int, vector<int>, less<int>> max_que;
        priority_queue<int, vector<int>, greater<int>> min_que;
        vector<int> ret;
        for (auto &n : nums)
        {
            if (max_que.empty() || n > max_que.top())
            {
                min_que.emplace(n);
                if (min_que.size() > max_que.size() + 1)
                {
                    max_que.emplace(min_que.top());
                    min_que.pop();
                }
            }
            else
            {
                max_que.emplace(n);
                if (max_que.size() > min_que.size())
                {
                    min_que.emplace(max_que.top());
                    max_que.pop();
                }
            }
            
            ret.emplace_back(max_que.size() == min_que.size() ? max_que.top() : min_que.top());
        }
        return ret;
    }
};

