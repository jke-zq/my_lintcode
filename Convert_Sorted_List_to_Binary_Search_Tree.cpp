/**
 * Definition of ListNode
 * class ListNode {
 * public:
 *     int val;
 *     ListNode *next;
 *     ListNode(int val) {
 *         this->val = val;
 *         this->next = NULL;
 *     }
 * }
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
     * @param head: The first node of linked list.
     * @return: a tree node
     */
    TreeNode *sortedListToBST(ListNode *head) {
        // write your code here
        auto pre = head;
        int length = 0;
        while (pre){
            ++length;
            pre = pre->next;
        }
        return doBuild(&head, 1, length);
    }
    TreeNode *doBuild(ListNode **head, int start, int end){
        if (start > end){
            return nullptr;
        }
        int mid = start + (end - start) / 2;
        TreeNode *left = doBuild(head, start, mid - 1);
        TreeNode *root = new TreeNode((*head)->val);
        root->left = left;
        *head = (*head)->next;
        root->right = doBuild(head, mid + 1, end);
        
        return root;
    }
};



