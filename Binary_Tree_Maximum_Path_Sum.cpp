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
     * @return: An integer
     */
    int maxPathSum(TreeNode *root) {
        // write your code here
        maxPathSumRecu(root);
        return max_sum_;
    }
    int maxPathSumRecu(TreeNode *root){
        if (!root) return 0;
        int left = max(0, maxPathSumRecu(root->left));
        int right = max(0, maxPathSumRecu(root->right));
        max_sum_ = max(max_sum_, root->val + left + right);
        return root->val + max(left, right);
    }
private:
    int max_sum_ = INT_MIN;
};
