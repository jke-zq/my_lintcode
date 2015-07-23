class Solution {
public:
   /**
     * @param A: An integer array
     * @return: Count the number of element before this element 'ai' is 
     *          smaller than it and return count number array
     */
    class BSTreeNode{
    public:
        int count;
        int value;
        BSTreeNode* left;
        BSTreeNode* right;
        BSTreeNode(int val){
            value = val;
            count = 0;
            left = nullptr;
            right = nullptr;
        }
    };
    vector<int> countOfSmallerNumberII(vector<int> &A) {
        // write your code here
        // 19/20 case Time Limit Exceeded
        // vector<int> result;
        // int length = A.size();
        // for(int i = 0; i < length; ++i){
        //     int count = 0;
        //     for(int j = 0; j < i; ++j){
        //         if(A[j] < A[i]) ++count;
        //     }
        //     result.emplace_back(count);
        // }
        // return result;
        if(A.size() == 0) return {};
        vector<int> result;
        BSTreeNode* root = new BSTreeNode(A[0]);
        result.emplace_back(0);
        for(int i = 1; i < A.size(); ++i){
            BSTreeNode* node = new BSTreeNode(A[i]);
            insert(root, node);
            int count = query(root, A[i]);
            result.emplace_back(count);
        }
        return result;
    }
    void insert(BSTreeNode* root, BSTreeNode* node){
        BSTreeNode* tmp = root;
        while(tmp){
            if(tmp->value > node->value){
                ++ tmp->count;
                if(tmp->left){
                    tmp = tmp->left;
                }else{
                    tmp->left = node;
                    break;
                }
            }else{
                if(tmp->right){
                    tmp = tmp->right;
                }else{
                    tmp->right = node;
                    break;
                }
            }
        }
    }
    int query(BSTreeNode* root, int val){
        int count = 0;
        BSTreeNode* tmp = root;
        while(tmp){
            if(tmp->value < val){
                count += 1 + tmp->count;
                tmp = tmp->right;
            }else if(tmp->value > val){
                tmp = tmp->left;
            }else{
                return count + tmp->count;
            }
        }
        
    }
};
