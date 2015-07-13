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
     * @return: Postorder in vector which contains node values.
     */
public:
    vector<int> postorderTraversal(TreeNode *root) {
        // write your code here
    //     vector<int> result;
    //     doOrder(root, result);
    //     return result;
    // }
    // void doOrder(TreeNode *node, vector<int>& vct){
    //     if(!node) return;
    //     if(node->left){
    //         doOrder(node->left, vct);
    //     }
    //     if(node->right){
    //         doOrder(node->right, vct);
    //     }
    //     vct.emplace_back(node->val);
    
        // write your code here using space(O(n)), time(O(n))
        // if(!root) return {};
        // stack<TreeNode*> path_stack;
        // path_stack.emplace(root);
        // TreeNode* pre = nullptr;
        // vector<int> result;
        // while(!path_stack.empty()){
        //     TreeNode* cur = path_stack.top();
        //     if(pre == nullptr || pre->left == cur || pre->right == cur){
        //         if(cur->left){
        //             path_stack.emplace(cur->left);
        //         }else if(cur->right){
        //             path_stack.emplace(cur->right);
        //         }else{
        //             result.emplace_back(cur->val);
        //             path_stack.pop();
        //         }
        //     }else if(cur->left == pre){
        //         if(cur->right){
        //             path_stack.emplace(cur->right);
        //         }else{
        //             result.emplace_back(cur->val);
        //             path_stack.pop();
        //         }
        //     }else{
        //         result.emplace_back(cur->val);
        //         path_stack.pop();
        //     }
        //     pre = cur;
        // }
        // return result;
        // write your code here using space(O(1)), time(O(n))
        vector<int> result;
        TreeNode dummy(INT_MIN);
        dummy.left = root;
        TreeNode* cur = &dummy;
        while(cur){
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
                    vector<int> res = dotravel(cur->left, node);
                    result.insert(result.end(), res.begin(), res.end());
                    node->right = nullptr;
                    cur = cur->right;
                }
            }
        }
        return result;
    }
    vector<int> dotravel(TreeNode* from, TreeNode* to){
        vector<int> res;
        TreeNode* cur = from;
        while(cur != to){
            res.emplace_back(cur->val);
            cur = cur->right;
        }
        res.emplace_back(cur->val);
        reverse(res.begin(), res.end());
        return res;
    }
};
