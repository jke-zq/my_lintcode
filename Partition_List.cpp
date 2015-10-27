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
     * @param x: an integer
     * @return: a ListNode 
     */
    ListNode *partition(ListNode *head, int x) {
        // write your code here
        //origin relative order
        // ListNode *dummy = new ListNode(INT_MIN);
        // dummy->next = head;
        // head = dummy;
        // while (head->next){
        //     if (head->next->val >= x){
        //         head = head->next;
        //     }else {
        //         auto temp = head->next;
        //         head->next = temp->next;
        //         // head = head->next;
        //         temp->next = dummy->next;
        //         dummy->next = temp;
        //     }
        // }
        // return dummy->next;
        //origin relative order
        ListNode* dummy = new ListNode(INT_MIN);
        dummy->next = head;
        auto pre = dummy, post = dummy;
        while (pre->next){
            if (pre->next->val < x){
                if (pre == post){
                    pre = pre->next;
                    post = post->next;
                }else {
                    auto temp = pre->next;
                    pre->next = temp->next;
                    temp->next = post->next;
                    post->next = temp;
                    post = post->next;
                }
            }else {
                pre = pre->next;
            }
        }
        return dummy->next;
    }
};



