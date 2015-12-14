class Solution {
public:
    /**
     * @param n an integer
     * @return true if this is a happy number or false
     */
    bool isHappy(int n) {
        // Write your code here
        unordered_set<int> result;
        int x = n;
        while (x != 1 && result.find(x) == result.end())
        {
            result.insert(x);
            x = next(x);
        }
        
        if (x == 1)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
    int next(int x)
    {
        int result = 0;
        while (x > 0)
        {
            int last = x % 10;
            result += last * last;
            x = x / 10;
        }
        return result;
    }
};