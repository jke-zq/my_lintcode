
/**
*NOTE:
*    more details from:http://articles.leetcode.com/2011/11/longest-palindromic-substring-part-ii.html
*    the point is that:given string "dsed...b...c1...a...c2...b...dwed" and "b...c1...a...c2...b" is palindromic. 
*    c1 and c2 is symmetric by char 'a', so c1 == c2. And because of the symmetric property of palidromic string, 
*    maybe the palindromic length of c2 is the same as the one of c1. But if the palindromic length is larger than "b...c1", 
*    we can get the palidromic length of c2 by increasing the length of "b...c1".
*/


class Solution {
public:
    /**
     * @param s input string
     * @return the longest palindromic substring
     */
    string longestPalindrome(string& s) {
        // Write your code here
        //o(n*n)
    //     int re_length = 1;
    //     string result = s.substr(0,1);
    //     for(int i = 0; i < s.size(); ++i){
    //         int start = i - 1;
    //         int end = i + 1;
    //         doWhile(start, end, re_length, result, s);
    //         end = i + 1;
    //         if(end < s.size() && s[i] == s[end]){
    //             start = i;
    //             doWhile(start, end, re_length, result, s);
    //         }
    //         start = i - 1;
    //         if(start > -1 && s[start] == s[i]){
    //             end = i;
    //             doWhile(start, end, re_length, result, s);
    //         }
    //     }
    //     return result;
    // }
    // void doWhile(int start, int end, int& re_length, string& result, string& s){
    //     while(start > -1 && end < s.size() && s[start] == s[end]){
    //         --start;
    //         ++end;
    //     }
    //     if(!(start > -1 && end < s.size())){
    //         ++start;
    //         --end;
    //     }else if(s[start] != s[end]){
    //         ++start;
    //         --end;
    //     }
    //     if(re_length < end - start + 1){
    //         re_length = end - start + 1;
    //         result = s.substr(start, re_length);
    //     }
        //o(n)

        string T = "^";
        if(s.empty()) T += "$";
        else{
            for(auto c : s){
                T += "#";
                T.push_back(c);
            }
            T += "#$";
        }
        int n = T.length();
        int center = 0;
        int right = 0;
        vector<int> palindromic(n, 0);
        for(int i = 1; i < n-1; ++i){
            int i_mirror = 2 * center - i;
            palindromic[i] = (right > i) ? min(right - i, palindromic[i_mirror]) : 0;
            while(T[i + palindromic[i] + 1] == T[i - palindromic[i] - 1])
                ++palindromic[i];
            if(i + palindromic[i] > right){
                center = i;
                right = i + palindromic[i];
            }
        }
        int max_length = 0;
        center = 0;
        for(int i = 0; i < palindromic.size(); ++i){
            if(palindromic[i] > max_length){
                max_length = palindromic[i];
                center = i;
            }
        }
        return s.substr((center - 1 - max_length)/2, max_length);
    }
};
