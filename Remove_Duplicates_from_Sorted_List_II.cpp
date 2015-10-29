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
class Solution{
public:
    /**
     * @param head: The first node of linked list.
     * @return: head node
     */
    ListNode * deleteDuplicates(ListNode *head) {
        // write your code here
        // ListNode *dummy = new ListNode(INT_MIN);
        // dummy->next = head;
        // ListNode *cp = dummy;
        // while (head){
        //     if (cp->next != head){
        //         if (head->val != cp->next->val){
        //             cp = cp->next;
        //             head = head->next;
        //         }else {
        //             auto temp = cp->next;
        //             while (head && head->val == temp->val){
        //                 delete temp;
        //                 temp = head;
        //                 head = head->next;
        //             }
        //             delete temp;
        //             cp->next = head;
        //         }
        //     }else {
        //         head = head->next;
        //     }
        // }
        // return dummy->next;
        ListNode *dummy = new ListNode(INT_MIN);
        dummy->next = head;
        auto pre = dummy;
        while (head){
            if (head->next && head->next->val == head->val){
                auto val = head->val;
                while (head && head->val == val){
                    auto temp = head;
                    head = head->next;
                    delete temp;
                }
                pre->next = head;
            }else {
                pre->next = head;
                pre = head;
                head = head->next;
            }
        }
        return dummy->next;
    }
};
