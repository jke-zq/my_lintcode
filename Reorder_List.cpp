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
 */
class Solution {
public:
    /**
     * @param head: The first node of linked list.
     * @return: void
     */
    void reorderList(ListNode *head) {
        // write your code here
        //left-middle and reverse middle-right
        ListNode *dummy = new ListNode(INT_MIN);
        dummy->next = head;
        ListNode *fast = dummy, *slow = dummy;
        while (fast && fast->next){
            slow = slow->next;
            fast = fast->next->next;
        }
        auto temp = slow;
        slow = slow->next;
        temp->next = nullptr;
        
        
        //slow is the head of the mid-right
        //reverse it
        ListNode *right_dummy = new ListNode(INT_MIN);
        auto new_dummy = right_dummy;
        while (slow){
            auto temp = slow;
            slow = slow->next;
            temp->next = right_dummy->next;
            right_dummy->next = temp;
        }
        //combination
        ListNode *right = new_dummy->next;
        head = dummy->next;
        while (right){
            auto temp = right;
            right = right->next;
            temp->next = head->next;
            head->next = temp;
            head = head->next->next;
        }
        
        head = dummy->next;
    }
};



