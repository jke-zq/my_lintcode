class Solution {
public:
    /**
     * @param A: an integer array.
     * @param k: a positive integer (k <= length(A))
     * @param target: a integer
     * @return an integer
     */
    int kSum(vector<int> A, int k, int target) {
        // wirte your code here
        //Time Limit Exceeded 7/40
    //     sort(A.begin(), A.end());
    //     int result = 0;
    //     doKSum(A, k, 0, target, result);
    //     return result;
    // }
    
    // void doKSum(vector<int>& A, int k, int position, int target, int& result){
    //     if(k < 0 || target < 0) return;
    //     if(k == 0 && target == 0){
    //         ++result; return;
    //     }
    //     for(int i = position; i < A.size() - k + 1; ++i){
    //         doKSum(A, k-1, i + 1, target - A[i], result);
    //     }
        //table[i][j][p]:i-> from A[0] to A[j] find i nums, and summation of i nums is p
        vector<vector<vector<int>>> table(2, vector<vector<int>>(A.size(), vector<int>(target+1, 0)));
        for(int i = 0; i < A.size(); ++i){
            if(A[i] <= target){
              for(int j = i; j < A.size(); ++j){
                  table[0][j][A[i]] = 1;
              }  
            }
        }
        
        for(int i = 1; i < k; ++i){
            for(int j = i; j < A.size(); ++j){
                for(int p = 1; p <= target; ++p){
                    table[i%2][j][p] = 0;//clear the data because of the reuse
                    if(i < j){
                        //if j > j - 1 >= i: val(j) = val(j-1) + others
                        table[i%2][j][p] = table[i%2][j-1][p];
                    }
                    if(p > A[j]){//[j][p] --- [j-1][p-A[j]] so, p != p - A[j] if A is unique ascending order int array
                        table[i%2][j][p] += table[(i-1)%2][j-1][p-A[j]];
                    }
                }
            }
        }
        
        return table[(k-1)%2][A.size()-1][target];
        
    }
};
