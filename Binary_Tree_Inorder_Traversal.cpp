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
    /**
     * @param root: The root of binary tree.
     * @return: Inorder in vector which contains node values.
     */
public:
    vector<int> inorderTraversal(TreeNode *root) {
        // write your code here
        // stack<TreeNode*> vn;
        // vector<int> result;
        // TreeNode * cur = root;
        // while(!vn.empty() || cur){

        //     if(cur){
        //         vn.emplace(cur);
        //         cur = cur->left;
        //     }else{
        //         cur = vn.top();
        //         vn.pop();
        //         result.emplace_back(cur->val);
        //         cur = cur->right;
        //     }
        // }
        // return result;
        vector<int> result;
        TreeNode* cur = root;
        while(cur){
            if(!cur->left){
                result.emplace_back(cur->val);
                cur = cur->right;
            }else{
                TreeNode* node = cur->left;
                while(node->right && node->right != cur){
                    node = node->right;
                }
                if(!node->right){
                    node->right = cur;
                    cur = cur->left;
                }else{
                    result.emplace_back(cur->val);
                    node->right = nullptr;
                    cur = cur->right;
                }
            }
        }
        return result;
    }
};
