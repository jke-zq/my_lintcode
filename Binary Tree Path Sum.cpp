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
     * @param root the root of binary tree
     * @param target an integer
     * @return all valid paths
     */
    vector<vector<int>> binaryTreePathSum(TreeNode *root, int target) {
        // Write your code here
        vector<vector<int>> ret;
        vector<int> tmp;
        doFind(0, root, tmp, ret, target);
        return ret;
    }
    void doFind(int sum, TreeNode *root, vector<int> &tmp, vector<vector<int>> &ret, int target)
    {
        if (!root)
        {
            if (sum == target)
            {
                ret.emplace_back(tmp);   
            }
            return;
        }
        else
        {
            tmp.emplace_back(root->val);
            if (!root->left && !root->right)
            {
                doFind(sum + root->val, root->left, tmp, ret, target);
            }
            else
            {
                doFind(sum + root->val, root->left, tmp, ret, target);
                doFind(sum + root->val, root->right, tmp, ret, target);                
            }
            tmp.pop_back();
        }
        
    }
};
