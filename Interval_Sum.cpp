/**
 * Definition of Interval:
 * classs Interval {
 *     int start, end;
 *     Interval(int start, int end) {
 *         this->start = start;
 *         this->end = end;
 *     }
 */
class Solution { 
public:
    /**
     *@param A, queries: Given an integer array and an query list
     *@return: The result list
     */
    class BSTreeNode{
    public:
        long long sum;
        int start;
        int end;
        BSTreeNode* left;
        BSTreeNode* right;
        BSTreeNode(int start, int end){
            sum = 0;
            this->start = start;
            this->end = end;
            left = right = nullptr;
        }
    };
    vector<long long> intervalSum(vector<int> &A, vector<Interval> &queries) {
        // write your code here
        BSTreeNode * root = buildBSTreeNode(A, 0, A.size()-1);
        vector<long long> result;
        for(auto& interval : queries){
            result.emplace_back(query(root, interval.start, interval.end));
        }
        return result;
    }
    BSTreeNode* buildBSTreeNode(vector<int> &A, int start, int end){
        if(end > start){
            BSTreeNode* root = new BSTreeNode(start, end);
            BSTreeNode* left = buildBSTreeNode(A, start, start + (end - start) / 2);
            BSTreeNode* right = buildBSTreeNode(A, start + (end - start) / 2 + 1, end);
            root->left = left;
            root->right = right;
            root->sum = left->sum + right->sum;
            return root;
        }else if(end == start){
            BSTreeNode* root = new BSTreeNode(start, end);
            root->sum = (long long)A[start];
            return root;
        }
        return nullptr;
    }
    
    long long query(BSTreeNode* root, int start, int end){
        if(root && root->start >= start && root->end <= end){
            return root->sum;
        }else if(!root || root->start > end || root->end < start){
            return 0;
        }else{
            return query(root->left, start, end) + query(root->right, start, end);
        }
        return 0;
    }
};
