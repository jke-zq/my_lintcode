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
     * @param A and B: two nodes in a Binary.
     * @return: Return the least common ancestor(LCA) of the two nodes.
     */
    TreeNode *lowestCommonAncestor(TreeNode *root, TreeNode *A, TreeNode *B) {
        // write your code here
        // unordered_map<TreeNode *, TreeNode *> map;
        // findAncestor(root, map);
        // unordered_set<TreeNode *> set;
        // TreeNode **p_A = &A;
        // set.insert(A);
        // while (map.find(*p_A) != map.end())
        // {
        //     set.insert(map[*p_A]);
        //     *p_A = map[*p_A];
        // }
        
        // p_A = &B;
        // while (set.find(*p_A) == set.end())
        // {
        //     *p_A = map[*p_A];
        // }
        
        // return *p_A;
        pair<int, TreeNode *> result = doFind(root, A, B);
        return result.second;
    }
    
    pair<int, TreeNode *> doFind(TreeNode *root, TreeNode *A, TreeNode *B)
    {
        if (!root)
        {
            return {0, nullptr};
        }
        
        auto leftFind = doFind(root->left, A, B);
        if (leftFind.first == 2)
        {
            return leftFind;
        }
        auto rightFind = doFind(root->right, A, B);
        if (rightFind.first == 2)
        {
            return rightFind;
        }
        int first = leftFind.first + rightFind.first + (root == A) + (root == B);
        return {first, first == 2 ? root : nullptr};
    }
    void findAncestor(TreeNode *root, unordered_map<TreeNode *, TreeNode *> &map)
    {
        if (!root)
        {
            return;
        }
        else
        {
            if (root->right)
            {
                map[root->right] = root;
                findAncestor(root->right, map);
            }
            if (root->left)
            {
                map[root->left] = root;
                findAncestor(root->left, map);
            }
        }
    }
};
