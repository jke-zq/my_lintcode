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
     * @param root the root of binary tree.
     * @return an integer
     */
    int maxPathSum2(TreeNode *root) {
        // Write your code here
        if (root == nullptr)
        {
            return 0;
        }
        return max(root->val, max(maxPathSum2(root->left), maxPathSum2(root->right)) + root->val);
    }
};

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
class Solution:
    """
    @param root the root of binary tree.
    @return an integer
    """
    def maxPathSum2(self, root):
        # Write your code here
        
        # def traverse(node, val):
        #     if not node:
        #         return val
        #     self.ret = max(self.ret, val)
        #     if node.left:
        #         traverse(node.left, val + node.left.val)
        #     if node.right:
        #         traverse(node.right, val + node.right.val)
        
        # if not root:
        #     return None
        # self.ret = float('-inf')
        # traverse(root, root.val)
        # return self.ret
        
        def traverse(node, val):
            if not node:
                return 0
            val = val + node.val
            ret[0] = max(ret[0], val)
            traverse(node.left, val)
            traverse(node.right, val)
        
        ret = [float('-inf')]
        traverse(root, 0)
        return ret[0]