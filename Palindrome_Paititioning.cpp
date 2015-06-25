/**
*NOTE:
*     Finding all possibilities is using DFS, and u can use this solution as a template.
*/


class Solution {
public:
    /**
     * @param s: A string
     * @return: A list of lists of string
     */
    vector<vector<string>> partition(string s) {
        // write your code here
        int length = s.length();
        vector<vector<string>> result;
        vector<string> tmp;
        helper(s, 0, length, tmp, result);
        return result;
    }
    
    void helper(string& s, int start, int length, vector<string>& tmp, vector<vector<string>>& result){
        if(start == length){
            result.emplace_back(tmp);
            return;
        }
        for(int i = start; i < length; ++i){
            if(check(s, start, i)){
                tmp.emplace_back(s.substr(start, i - start + 1));
                helper(s, i+1, length, tmp, result);
                tmp.pop_back();
            }
        }
    }
    bool check(string& s, int start, int end){
        while(start <= end){
            if(s[start] == s[end]){
                ++start;
                --end;
            }
            else return false;
        }
        return true;
    }
    
};
