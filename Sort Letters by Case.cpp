class Solution {
public:
    /** 
     * @param chars: The letters array you should sort.
     */
    void sortLetters(string &letters) {
        // write your code here
        int len = letters.length();
        int left = 0, right = len - 1;
        while (left < right)
        {
            while (left < right && islower(letters[left]))
            {
                ++left;
            }
            while (left < right && isupper(letters[right]))
            {
                --right;
            }
            swap(letters[left], letters[right]);
            ++left;
            --right;
        }
    }
};
