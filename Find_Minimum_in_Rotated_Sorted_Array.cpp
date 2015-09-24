class Solution {
public:
    /**
     * @param num: a rotated sorted array
     * @return: the minimum number in the array
     */
    int findMin(vector<int> &num) {
        // write your code here
        int s = 0;
        int e = num.size() - 1;
        while (s < e && num[s] > num[e]){
            int m = s + (e - s) / 2;
            if (num[m] >= num[s]){
                s = m + 1;
            }else{
                e = m;
            }
        }
        //[1,2,3] s = 0; [3,2,1] s != num.size() - 1, but min the two values.
        return min(num[s], num[num.size() - 1]);
    }
};
