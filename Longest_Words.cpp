/**
*NOTE:
*     string.length return value with type size_t, cant cmpare with the int type value.
*     more details about size_t in cpp_details/size_t.
*     more details about vector in cpp_details/vector.
*/
class Solution {
public:
    /**
     * @param dictionary: a vector of strings
     * @return: a vector of strings
     */
    vector<string> longestWords(vector<string> &dictionary) {
        // write your code here
        vector<string> result;
        for(const auto& s : dictionary){
            if(!result.empty() && s.length() > result[0].length()){
                result.clear();
                result.emplace_back(s);
            }else if(result.empty() || s.length() == result[0].length()){
                result.emplace_back(s);
            }
        }
        return result;
    }
};
