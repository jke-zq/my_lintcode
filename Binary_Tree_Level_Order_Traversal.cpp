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
     * @return: Level order a list of lists of integer
     */
public:
    vector<vector<int>> levelOrder(TreeNode *root) {
        // write your code here
        vector<vector<int>> ret;
        vector<int> cur_lev;
        queue<TreeNode *> queue;
        if (root){
            queue.emplace(root);
        }
        int cur_lev_cnt = queue.size();
        while (!queue.empty()){
            TreeNode *root = queue.front();
            queue.pop();
            cur_lev.emplace_back(root->val);
            --cur_lev_cnt;
            if (root->left){
                queue.emplace(root->left);
            }
            if (root->right){
                queue.emplace(root->right);
            }
            if (cur_lev_cnt == 0){
                ret.emplace_back(move(cur_lev));
                cur_lev_cnt = queue.size();
            }
            
        }
        return ret;

    }
};

