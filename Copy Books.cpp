class Solution {
public:
    /**
     * @param pages: a vector of integers
     * @param k: an integer
     * @return: an integer
     */
    int copyBooks(vector<int> &pages, int k) {
        // write your code here
        //binary search-- good example: if valid: right = mid - 1 else left = mid + 1; valid func is the only condition of any case;
        if (k >= pages.size())
        {
            return *max_element(pages.cbegin(), pages.cend());
        }
        else
        {
            int sum = 0;
            for (const auto &p : pages)
            {
                sum += p;
            }
            int average = sum / k;
            return binarySearch(pages, k, average, sum);
        }
    }
    int binarySearch(const vector<int> &pages, int k, int left, int right)
    {
        while (left < right)
        {
            int mid = left + (right - left) / 2;
            if (valid(pages, k, mid))
            {
                right = mid;
            }
            else
            {
                left = mid + 1;
            }
        }
        return right;
    }
    bool valid(const vector<int> &pages, const int k, int mid)
    {
        int sum = 0;
        int ps = 0;
        for (const auto &p : pages)
        {
            if (sum + p > mid)
            {
                sum = 0;
                ++ps;
            }
            sum += p;
        }
        //the last people
        ++ps;
        return sum <= mid && ps <= k;
    }
};