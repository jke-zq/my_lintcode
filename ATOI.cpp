
/**
*NOTE:
*     Because I dont deeply understand the question, I update the solution according to the unpassed case.
*/

class Solution {
public:
    /**
     * @param str: A string
     * @return An integer
     */
    int atoi(string str) {
        // write your code here
        long result = 0L;
        int tag = 0;
        for(auto& s : str){
            if(s == '-' || s == '+'){
                if(result != 0L) break;
                if(tag != 0) return 0;
                tag = s == '-' ? -1 : 1;
                continue;
            }
            if(s == '.') break;
            if(s == ' ') continue;
            if(!isdigit(s)) break;
            result  = result * 10 + s - '0';
            if(result > INT_MAX) return tag < 0 ? INT_MIN : INT_MAX;
        }
        return result * (tag == 0 ? 1 : tag);
    }


    //other's solution, very good.
    if(str.empty()) return 0;
    int sign = 1;
    int result = 0;
    int i = 0;
    while(str[i] == ' ') ++i;
    if(str[i] == '-'){
        sign = -1;
        ++i;
    }
    else if(str[i] == '+'){
        sign = 1;
        ++i;
    }
    for(; i < str.length() && isdigit(str[i]); ++i){
        if(result > (INT_MAX - str[i] + '0') / 10 || (result == INT_MAX / 10 && INT_MAX % 10 < str[i] - '0')) return sign > 0 ? INT_MAX : INT_MIN;
        result *= 10;
        result += str[i] - '0';
    }
    return result * sign;
};
