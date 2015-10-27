/**
 * Definition of ListNode
 * 
 * class ListNode {
 * public:
 *     int val;
 *     ListNode *next;
 * 
 *     ListNode(int val) {
 *         this->val = val;
 *         this->next = NULL;
 *     }
 * }
 */
class Solution {
public:
    /**
     * @param head: The first node of linked list.
     * @return: The new head of reversed linked list.
     */
    ListNode *reverse(ListNode *head) {
        // write your code here
        if (!head) return head;
        ListNode *left = head, *right = head->next;
        if (!right) return head;
        left->next = nullptr;
        while (right->next){
            auto temp = right;
            right = right->next;
            temp->next = left;
            left = temp;
        }
        right->next = left;
        return right;
    }
};

