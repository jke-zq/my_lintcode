class Solution {
public:
    /**
     * @param A: A list of lists of integers
     * @return: An integer
     */
    int jump(vector<int> A) {
        // wirte your code here
        int max_len = 1 + A[0];
        int step = 1;
        
        for (int i = 0; i <= max_len; ++i){
            if (max_len >= A.size()) return step;
            if (i + A[i] > max_len){
                max_len = i + A[i];
                ++step;
            }
        }
        return step;
    }
};