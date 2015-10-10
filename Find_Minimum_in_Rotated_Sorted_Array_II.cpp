class Solution {
public:
    /**
     * @param num: the rotated sorted array
     * @return: the minimum number in the array
     */
    int findMin(vector<int> &num) {
        // write your code here
        int s = 0;
        int e = num.size() - 1;
        while (s < e && num[s] >= num[e]){
            int m = s + (e - s) / 2;
            // if (num[m] <= num[e] && num[m] != num[s]){
            //     e = m;
            // }else{
            //     s = m + 1;
            // }
            if (num[s] <= num[m]){
                s = m + 1;
            }else {
                e = m;
            }
        }
        return num[s];
    }
};
