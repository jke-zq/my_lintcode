class Solution {
public:
    /**
     * @param A a string
     * @param B a string
     * @return a boolean
     */
    bool stringPermutation(string& A, string& B) {
        // Write your code here
        unordered_map<char, int> count;
        for (const auto &a : A)
        {
            ++count[a];
        }
        for (const auto &b : B)
        {
            if (count.find(b) == count.end())
            {
                return false;
            }
            else
            {
                --count[b];
                if (count[b] == 0)
                {
                    count.erase(b);
                }
            }
        }
        return count.size() == 0;
    }
};