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
     * @param root: The root of binary tree.
     * @return: True if the binary tree is BST, or false
     */
    bool isValidBST(TreeNode *root) {
        // write your code here
        // return doValidBST(root, (long)INT_MIN - 1, (long)INT_MAX + 1);
        //using inorder to check
        if (!root){
            return true;
        }
        if (!isValidBST(root->left)){
            return false;
        }
        //remove && last != root, last never same to root
        if (last && last->val >= root->val){
            return false;
        }
        last = root;
        if (!isValidBST(root->right)){
            return false;
        }
        return true;
    }
    // bool doValidBST(TreeNode *root, long down, long up){
    //     if (!root) return true;
    //     bool left = true;
    //     if (!(root->val > down && root->val < up)){
    //         return false;
    //     }
    //     if (root->left){
    //         left = doValidBST(root->left, down, root->val);
    //     }
    //     if (!left) return false;
        
    //     bool right = true;
    //     if (root->right){
    //         right = doValidBST(root->right, root->val, up);
    //     }
        
    //     return right;
    // }
private:
    TreeNode *last = nullptr;
};
