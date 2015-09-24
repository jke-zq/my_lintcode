class Solution {
public:
    /** 
     *@param L: Given n pieces of wood with length L[i]
     *@param k: An integer
     *return: The maximum length of the small pieces.
     */
    int woodCut(vector<int> L, int k) {
        // write your code here
        if (L.empty()) return 0;
        // sort(L.begin(), L.end());
        int low = 1;
        // int high = L[L.size() - 1];
        int high = *max_element(L.cbegin(), L.cend());
        while (low <= high){
            int mid = low + (high - low) / 2;
            //check the number >= k
            int num = 0;
            for (const auto& len : L){
                num += len / mid;
            }
            if (num >= k){
                low = mid + 1;
            }else{
                high = mid - 1;
            }
        }
        return low - 1;
    }
};
