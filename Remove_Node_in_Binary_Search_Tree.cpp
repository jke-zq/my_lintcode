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
     * @param value: Remove the node with given value.
     * @return: The root of the binary search tree after removal.
     */
    TreeNode* removeNode(TreeNode* root, int value) {
        // write your code here
        if (!root)
        {
            return nullptr;
        }
        if (root->val > value)
        {
            root->left = removeNode(root->left, value);
        }
        else if (root->val < value)
        {
            root->right = removeNode(root->right, value);
        }
        else
        {
            if (!root->left)
            {
                return root->right;
            }
            else if (!root->right)
            {
                return root->left;
            }
            TreeNode *cp = root;
            root = findAndDelMaxLeft(root->left);
            root->right = cp->right;
        }
        return root;
    }
    
    TreeNode *findAndDelMaxLeft(TreeNode *root)
    {
        TreeNode *parent;
        TreeNode *cp = root;
        while (root && root->right)
        {
            parent = root;
            root = root->right;
        }
        if (root != cp)
        {
            parent->right = root->left;
            root->left = cp;
        }
        return root;
    }
};
