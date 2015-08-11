class Solution {
public:
    /**
     * @param nums: The integer array
     * @return: The length of LIS (longest increasing subsequence)
     */
    int longestIncreasingSubsequence(vector<int> nums) {
        // write your code here
        //copy from others and misunderstand the question...
        vector<int> LIS;
        for(auto& i : nums){
            insert(LIS, i);
        }
        return LIS.size();
    }
    void insert(vector<int>& LIS, int target){
        int left = 0, right = LIS.size() - 1;
        auto compare = [](int source, int target){ return source <= target;};
        while(left <= right){
            int mid = left + (right - left) / 2;
            if(!compare(LIS[mid], target)){
                right = mid - 1;
            }else{
                left = mid + 1;
            }
        }
        if(left == LIS.size()){
            LIS.emplace_back(target);
        }else{
            LIS[left] = target;
        }
    }
};
