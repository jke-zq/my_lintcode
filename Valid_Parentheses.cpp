/**
*NOTE:
*    map is good to check diffrent condition;
*/

#include <unordered_map>
class Solution {
public:
    /**
     * @param s A string
     * @return whether the string is a valid parentheses
     */
    bool isValidParentheses(string& s) {
        // Write your code here
        vector<char> result;
        unordered_map<char, char> map;
        map.emplace('}', '{');
        map.emplace(')', '(');
        map.emplace(']', '[');
        for(auto& c : s){
            if(map.find(c) != map.end()){
                if(result.size() > 0 && result.back() == map[c]){
                    result.pop_back();
                }else return false;
            }else result.emplace_back(c);
        }
        if(result.size() > 0) return false;
        return true;
    }
};
