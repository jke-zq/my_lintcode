/**
 * Definition of TreeNode:
 * class TreeNode {
 * public:
 *     int val;
 *     TreeNode *left, *right;
 *     TreeNode(int val) {
 *         this->val = val;
 *         this->left = this->right = NULL;
 *     }
 * }
 */
class Solution {
public:
    /**
     * @param root: The root of the binary search tree.
     * @param k1 and k2: range k1 to k2.
     * @return: Return all keys that k1<=key<=k2 in ascending order.
     */
    vector<int> searchRange(TreeNode* root, int k1, int k2) {
        // write your code here
        vector<int> ret;
        doSearchRange(root, k1, k2, ret);
        return ret;
    }
    
private:
    void doSearchRange(TreeNode *root, const int k1, const int k2, vector<int>& ret){
        if (!root){
            return;
        }
        doSearchRange(root->left, k1, k2, ret);
        if (root->val >= k1 && root->val <= k2){
            ret.emplace_back(root->val);
        }
        doSearchRange(root->right, k1, k2, ret);
    }
};
