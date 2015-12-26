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
 * Example of iterate a tree:
 * BSTIterator iterator = BSTIterator(root);
 * while (iterator.hasNext()) {
 *    TreeNode * node = iterator.next();
 *    do something for node
 */
class BSTIterator {
private:
    stack<TreeNode *> s;
public:
    //@param root: The root of binary tree.
    BSTIterator(TreeNode *root) {
        // write your code here
        TreeNode *tmp = root;
        while (tmp)
        {
            s.emplace(tmp);
            tmp = tmp->left;
        }
        
    }

    //@return: True if there has next node, or false
    bool hasNext() {
        // write your code here
        return s.size() > 0;
    }
    
    //@return: return next node
    TreeNode* next() {
        // write your code here
        TreeNode *ret = s.top();
        s.pop();
        TreeNode *right = ret->right;
        while (right)
        {
            s.emplace(right);
            right = right->left;
        }
        return ret;
    }
};