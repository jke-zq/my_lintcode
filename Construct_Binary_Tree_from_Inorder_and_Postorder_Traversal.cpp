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
     *@param inorder : A list of integers that inorder traversal of a tree
     *@param postorder : A list of integers that postorder traversal of a tree
     *@return : Root of a tree
     */
public:
    TreeNode *buildTree(vector<int> &inorder, vector<int> &postorder) {
        // write your code here
        unordered_map<int, int> map;
        for (int i = 0; i < inorder.size(); ++i)
        {
            map[inorder[i]] = i;
        }
        return doBuildTree(postorder, 0, postorder.size() - 1, inorder, 0, inorder.size() - 1, map);
    }
private:
    TreeNode *doBuildTree(const vector<int>& postorder, int poss, int pose, const vector<int>& inorder, int ins, int ine, const unordered_map<int, int> map)
    {
        TreeNode *root = nullptr;
        if (poss <= pose && ins <= ine)
        {
            int index = map.at(postorder[pose]);
            int size = index - ins;
            root = new TreeNode(postorder[pose]);
            root->left = doBuildTree(postorder, poss, poss + size - 1, inorder, ins, ins + size - 1, map);
            root->right = doBuildTree(postorder, poss + size, pose - 1, inorder, ins + size + 1, ine, map);
        }
        return root;
    }
};
