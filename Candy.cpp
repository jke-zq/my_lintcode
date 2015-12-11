class Solution {
public:
    /**
     * @param ratings Children's ratings
     * @return the minimum candies you must give
     */
    int candy(vector<int>& ratings) {
        // Write your code here
        // if (ratings.empty())
        // {
        //     return 0;
        // }
        // int size = ratings.size();
        // vector<int> candies(size);
        // for (int i = 0; i < size; ++i)
        // {
        //     candies[i] = 1;
        //     int j = i;
        //     while (j > -1 && ratings[j] < ratings[j - 1] && candies[j - 1] <= candies[j])
        //     {
        //         ++candies[j - 1];
        //         --j;
        //     }
        //     if (i > -1 && ratings[i] > ratings[i - 1])
        //     {
        //         candies[i] += candies[i - 1];
        //     }
        // }
        // int ret = 0;
        // for (auto &c : candies)
        // {
        //     ret += c;
        // }
        // return ret;
        int size = ratings.size();
        vector<int> candies(size, 1);
        for (int i = 1; i < size; ++i)
        {
            if (ratings[i] > ratings[i - 1])
            {
                candies[i] = candies[i - 1] + 1;
            }
        }
        for (int i = size - 2; i >= 0; --i)
        {
            if (ratings[i] > ratings[i + 1] && candies[i] <= candies[i + 1])
            {
                candies[i] = candies[i + 1] + 1;
            }
        }
        int ret = 0;
        for (auto &c : candies)
        {
            ret += c;
        }
        return ret;
    }
};