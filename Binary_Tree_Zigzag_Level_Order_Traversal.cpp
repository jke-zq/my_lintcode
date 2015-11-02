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
     * @return: A list of lists of integer include 
     *          the zigzag level order traversal of its nodes' values 
     */
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode *root) {
        // write your code here
        vector<vector<int>> output;
        queue<TreeNode *> queue;
        vector<int> cur_lev;
        if (root)
        {
            queue.emplace(root);
        }
        int cur_lev_cnt = queue.size();
        bool isLeftToRight = true;
        while (!queue.empty())
        {
            TreeNode *node = queue.front();
            --cur_lev_cnt;
            queue.pop();
            cur_lev.emplace_back(node->val);
            if (node->left)
            {
                queue.emplace(node->left);
            }
            if (node->right)
            {
                queue.emplace(node->right);
            }
            if (cur_lev_cnt == 0)
            {
                cur_lev_cnt = queue.size();
                if (!isLeftToRight){
                    reverse(cur_lev.begin(), cur_lev.end());
                }
                isLeftToRight = !isLeftToRight;
                output.emplace_back(move(cur_lev));
            }
        }
        return output;
    }
    
};
