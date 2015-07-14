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
     * @return: Preorder in vector which contains node values.
     */
    vector<int> preorderTraversal(TreeNode *root) {
        // write your code here
    //     vector<int> res;
    //     helper(root, res);
    //     return res;
    // }
    // void helper(TreeNode* node, vector<int>& res){
    //     if(!node) return;
    //     res.emplace_back(node->val);
    //     helper(node->left, res);
    //     helper(node->right, res);
        // write your code here space(O(n)) time(o(n))
        // stack<TreeNode*> path_stack;
        // TreeNode* cur = root;
        // vector<int> result;
        // while(!path_stack.empty() || cur){
        //     if(cur){
        //         result.emplace_back(cur->val);
        //         path_stack.emplace(cur);
        //         cur = cur->left;
        //     }else{
        //         cur = path_stack.top();
        //         path_stack.pop();
        //         cur = cur->right;
                
        //     }
        // }
        // return result;
        // write your code here space(o(1)) time(o(1))
        
        vector<int> res;
        TreeNode* cur = root;
        while(cur){
            res.emplace_back(cur->val);
            if(!cur->left){
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
                    node->right = nullptr;
                    cur = cur->right;
                    res.pop_back();
                }
            }
        }
        return res;
  
    }
};

