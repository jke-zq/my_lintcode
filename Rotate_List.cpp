/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    /**
     * @param head: the list
     * @param k: rotate to the right k places
     * @return: the list after rotation
     */
    ListNode *rotateRight(ListNode *head, int k) {
        // write your code here
        //get length
        int len = 0;
        auto temp = head;
        while (temp){
            temp = temp->next;
            ++len;
        }
        if (!len) return head;
        k = k % len;
        if (!k) return head;
        ListNode *dummy = new ListNode(INT_MIN);
        dummy->next = head;
        auto fast = dummy, slow = dummy;
        for (int i = 0; i < k; ++i){
            fast = fast->next;
        }
        while (fast->next){
            fast = fast->next;
            slow = slow->next;
        }
        head = slow->next;
        fast->next = dummy->next;
        slow->next = nullptr;
        delete dummy;
        return head;
    }
};
