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
     *@param preorder : A list of integers that preorder traversal of a tree
     *@param inorder : A list of integers that inorder traversal of a tree
     *@return : Root of a tree
     */
public:
    TreeNode *buildTree(vector<int> &preorder, vector<int> &inorder) {
        // write your code here
        unordered_map<int, size_t> in_entry_idx_map;
        for (size_t i = 0; i < inorder.size(); ++i){
            in_entry_idx_map.emplace(inorder[i], i);
        }
        return buildTreeHelper(preorder, 0, preorder.size() - 1, inorder, 0, inorder.size() - 1, in_entry_idx_map);
    }
    TreeNode *buildTreeHelper(const vector<int>& preorder, const int pres, const int pree, const vector<int>& inorder, const int ins, const int ine, const unordered_map<int, size_t>& in_entry_idx_map){
        if (pree >= pres && ine >= ins){
            int root_index = in_entry_idx_map.at(preorder[pres]);
            int size = root_index - ins;
            TreeNode *root = new TreeNode(preorder[pres]);
            root->left = buildTreeHelper(preorder, pres + 1, pres + size, inorder, ins, ins + size - 1, in_entry_idx_map);
            root->right = buildTreeHelper(preorder, pres + size + 1, pree, inorder, ins + size + 1, ine, in_entry_idx_map);
            return root;
        }
        return nullptr;
    }
};
