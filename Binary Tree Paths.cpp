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
     * @param root the root of the binary tree
     * @return all root-to-leaf paths
     */
    vector<string> binaryTreePaths(TreeNode* root) {
        // Write your code here
        string path;
        vector<string> ret;
        if (!root)
        {
            return ret;
        }
        doHelper(root, path, ret);
        return ret;
    }
    
    void doHelper(TreeNode *root, string s, vector<string> &ret)
    {
        if (!root->right && !root->left)
        {
            ret.emplace_back(s + to_string(root->val));
            return;
        }
        else
        {
            if (root->right)
            {
                doHelper(root->right, s + to_string(root->val) + "->", ret);    
            }
            if (root->left)
            {
                doHelper(root->left, s + to_string(root->val) + "->", ret);    
            }
            
        }
    }
};