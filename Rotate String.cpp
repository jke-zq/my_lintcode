class Solution {
public:
    /**
     * @param str: a string
     * @param offset: an integer
     * @return: nothing
     */
    void rotateString(string &str,int offset){
        //wirte your code here
        if (!str.empty())
        {
            offset = offset % str.length();
            reverse(str.begin(), str.end());
            reverse(str.begin(), str.begin() + offset);
            reverse(str.begin() + offset, str.end());
        }
    }
};

