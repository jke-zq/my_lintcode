class Solution {
public:
    /**
     * @param digits a number represented as an array of digits
     * @return the result
     */
    vector<int> plusOne(vector<int>& digits) {
        // Write your code here
        int weight = 1;
        for (int i = digits.size() - 1; i > -1; --i)
        {
            if (digits[i] + weight == 10)
            {
                digits[i] = 0;
            }
            else
            {
                digits[i] += weight;
                weight = 0;
                break;
            }
        }
        if (weight)
        {
            digits.emplace(digits.begin(), 1);
        }
        return digits;
    }
};