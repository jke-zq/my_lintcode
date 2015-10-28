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
     * @return: You should return the head of the sorted linked list,
                    using constant space complexity.
     */
    ListNode *sortList(ListNode *head) {
        // write your code here
        if (!head || !head->next){
            return head;
        }
        ListNode *fast = head;
        ListNode *slow = head;
        while (fast->next && fast->next->next){
            slow = slow->next;
            fast = fast->next->next;
        }
        fast = slow->next;
        slow->next = nullptr;
        slow = fast;
        return merge(sortList(head), sortList(slow));
    }
private:
    ListNode *merge(ListNode *list1, ListNode *list2){
        ListNode dummy(INT_MIN);
        auto head = &dummy;
        while (list1 && list2){
            if (list1->val > list2->val){
                head->next = list2;
                list2 = list2->next;
            }else {
                head->next = list1;
                list1 = list1->next;
            }
            head = head->next;
        }
        if (list1){
            head->next = list1;
        }
        if (list2){
            head->next = list2;
        }
        return dummy.next;
    }
};



