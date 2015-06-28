class Solution {
public:
    /**
     * @param s A string
     * @return the length of last word
     */
    int lengthOfLastWord(string& s) {
        // Write your code here
        int result = 0;
        for(auto& c : s){
            if(c == ' ')
                result = 0;
            else
                ++result;
        }
        return result;
    }
};
