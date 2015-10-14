class Solution {
public:
    /**
     *@param num: A list of non negative integers
     *@return: A string
     */
    string largestNumber(vector<int> &num) {
        // write your code here
        sort(num.begin(), num.end(), [](const int& i, const int& j){
            return to_string(i) + to_string(j) > to_string(j) + to_string(i);
        });
        string ret;
        for (const auto& n : num){
            ret.append(to_string(n));
        }
        if (ret[0] == '0'){
            return "0";
        }
        return ret;
    }
};