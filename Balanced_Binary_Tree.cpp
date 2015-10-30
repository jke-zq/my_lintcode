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
     * @return: True if this Binary tree is Balanced, or false.
     */
    bool isBalanced(TreeNode *root) {
        // write your code here
        return doCheck(root) < 0 ? false : true;
    }
    int doCheck(TreeNode *node){
        if (!node){
            return 0;
        }
        int left = doCheck(node->left);
        if (left < 0){
            return -1;
        }
        int right = doCheck(node->right);
        if (right < 0){
            return -1;
        } else if (abs(left - right) > 1){
            return -1;
        }else {
            return max(left, right) + 1;
        }
    }
};
