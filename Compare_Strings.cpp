class Solution {
public:
    /**
     * @param A: A string includes Upper Case letters
     * @param B: A string includes Upper Case letter
     * @return:  if string A contains all of the characters in B return true 
     *           else return false
     */
    bool compareStrings(string A, string B) {
        // write your code here
        // for(auto& s : B){
        //     if(!A.empty() && A.find(s) != string::npos){
        //         A.erase(A.find(s), 1);
        //     }else{
        //         return false;
        //     }
        // }
        // return true;
        //good solution
        unordered_map<char, int> canFound;
        for(auto& s : A)
            ++canFound[s];
        for(auto& s : B)
            if(--canFound[s] < 0)
                return false;
        return true;
    }
};