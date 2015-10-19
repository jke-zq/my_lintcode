class Solution {
public:
    /**
     *@param A: A positive integer which has N digits, A is a string.
     *@param k: Remove k digits.
     *@return: A string
     */
    string DeleteDigits(string A, int k) {
        // wirte your code here
        //solution1:O(n) space/time
        // if (A.length() <= k) return "0";
        // stack<char> s;
        // for (int i = 0; i < A.length(); ++i){
        //     while (k > 0 && !s.empty() && s.top() > A[i]){
        //         s.pop();
        //         --k;
        //     }
        //     s.emplace(A[i]);
        // }
        // while (k){
        //     s.pop();
        //     --k;
        // }
        // string ret;
        // while (!s.empty()){
        //     ret.push_back(s.top());
        //     s.pop();
        // }
        // reverse(ret.begin(), ret.end());
        // int i = 0;
        // for (; i < ret.length() && ret[i] == '0'; ++i);
        // ret = ret.substr(i);
        // if (ret.length() == 0){
        //     return "0";
        // }else {
        //     return ret;
        // }
        //solution2:O(k*n) time / O(1) space
        if (A.length() == k) return "0";
        int i = 0;
        while (i + 1 < A.length() && k > 0){
            if (A[i] > A[i + 1]){
                A.erase(A.begin() + i);
                i = max(0, i - 1);
                --k;
            }else {
                ++i;
            }
        }
        if (k > 0){
            A = A.substr(0, A.length() - k);
        }
        
        if (A.length() > 0 && A[0] == '0'){
            size_t pos = A.find_first_not_of("0");
            if (pos != string::npos){
                A = A.substr(pos);
            }
        }
        if (A.length() == 0){
            return "0";
        }
        return A;
        
    }
};

