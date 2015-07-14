class Solution {
public:
    /**
     * @param n: An integer
     * @return: An integer
     */
    // unordered_map<int,int> map;
    int climbStairs(int n) {
        // write your code here
        // if(n == 1) return 1;
        // if(n == 2) return 2;
        // if(map.find(n-1) == map.end()){
        //     map[n-1] = climbStairs(n-1);
        // }
        // if(map.find(n-2) == map.end()){
        //     map[n-2] = climbStairs(n-2);
        // }
        // return map[n-1] + map[n-2];
        int s[] = {1,2,0};
        int i = 2;
        while(i < n){
            s[i%3] = s[(i-1)%3] + s[(i-2)%3];
            ++i;
        }
        return s[(n-1)%3];
    }
};

