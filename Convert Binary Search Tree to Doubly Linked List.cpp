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
 * Definition of Doubly-ListNode
 * class DoublyListNode {
 * public:
 *     int val;
 *     DoublyListNode *next, *prev;
 *     DoublyListNode(int val) {
 *         this->val = val;
           this->prev = this->next = NULL;
 *     }
 * }
 */
class Solution {
public:
    /**
     * @param root: The root of tree
     * @return: the head of doubly list node
     */
    DoublyListNode* bstToDoublyList(TreeNode* root) {
        // Write your code here
        DoublyListNode dummy(INT_MIN);
        DoublyListNode *head = &dummy;
        doHelper(root, &head);
        //without the if-case, pass too. But, it should be remove the prev
        // if (dummy.next)
        // {
        //     dummy.next->prev = nullptr;
        // }
        return dummy.next;
    }
    
    void doHelper(TreeNode *root, DoublyListNode **head)
    {
        if (!root)
        {
            return;
        }
        doHelper(root->left, head);
        DoublyListNode *cur = new DoublyListNode(root->val);
        (*head)->next = cur;
        cur->prev = *head;
        *head = cur;
        doHelper(root->right, head);
        
    }
};



