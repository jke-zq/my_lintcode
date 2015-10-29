/**
 * Definition of singly-linked-list:
 * 
 * class ListNode {
 * public:
 *     int val;
 *     ListNode *next;
 *     ListNode(int val) {
 *        this->val = val;
 *        this->next = NULL;
 *     }
 * }
 */
class Solution {
public:
    /**
     * @param head: The head of linked list.
     * @param m: The start position need to reverse.
     * @param n: The end position need to reverse.
     * @return: The new head of partial reversed linked list.
     */
    ListNode *reverseBetween(ListNode *head, int m, int n) {
        // write your code here
        ListNode *dummy = new ListNode(INT_MIN);
        dummy->next = head;
        head = dummy;
        //move m-1 steps
        for (int i = m - 1; i > 0; --i){
            head = head->next;
        }
        auto tail = head->next;
        head->next = nullptr;//cut down
        //reverse n - m + 1 nodes
        auto pre = tail;
        for (int i = n - m + 1; i > 0; --i){
            auto temp = head->next;
            head->next = pre;
            pre = pre->next;
            head->next->next = temp;
            
        }
        //linked the tail with left
        tail->next = pre;
        return dummy->next;
    }
};

