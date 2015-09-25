/**
 * class VersionControl {
 *     public:
 *     static bool isBadVersion(int k);
 * }
 * you can use VersionControl::isBadVersion(k) to judge whether 
 * the kth code version is bad or not.
*/
class Solution {
public:
    /**
     * @param n: An integers.
     * @return: An integer which is the first bad version.
     */
    int findFirstBadVersion(int n) {
        // write your code here
        int s = 0;
        int e = n - 1;
        while (s <= e){
            int m = s + (e - s) / 2;
            if (!VersionControl::isBadVersion(m)){
                s = m + 1;
            }else{
                e = m - 1;
            }
        }
        return s;
    }
};

