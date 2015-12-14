class Solution {
public:
    /**
     * @param s A string
     * @return Whether the string is a valid palindrome
     */
    bool isPalindrome(string& s) {
        // Write your code here
        if (s.empty())
        {
            return true;
        }
        int left = 0, right = s.length() - 1;
        while (left < right)
        {
            while (left < right && !isalnum(s[left]))
            {
                ++left;
            }
            while (right > left && !isalnum(s[right]))
            {
                --right;
            }
            //the worse case: left == right, so
            if (toupper(s[right]) != toupper(s[left]))
            {
                return false;
            }
            else
            {
                ++left;
                --right;
            }
            // if (left <= right)
            // {
            //     if (toupper(s[right]) == toupper(s[left]))
            //     {
            //         --right;
            //         ++left;
            //     }
            //     else
            //     {
            //         return false;
            //     }
            // }

        }
        return true;
    }
};